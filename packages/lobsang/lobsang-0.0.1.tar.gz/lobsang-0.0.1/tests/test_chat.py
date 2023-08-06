import pytest

from lobsang import Chat, SystemMessage, UserMessage, AssistantMessage
from lobsang.directives import Directive
from lobsang.llms.fake import FakeLLM


class TestDirective(Directive):
    """
    Dummy directive for testing.
    """

    def embed(self, message: str) -> (str, dict):
        return f"embed {message}", {'original': message}

    def parse(self, response: str) -> (str, dict):
        return f"parse {response}", {'original': response}


@pytest.fixture
def chat():
    return Chat("You are a helpful assistant.", llm=FakeLLM())


def test_init():
    """
    Test __init__ method.
    """
    assert Chat("You are a helpful assistant.") == Chat(SystemMessage("You are a helpful assistant.")), \
        "Chat not initialized correctly."

    assert Chat([SystemMessage("You are a helpful assistant."), UserMessage("My name is Bark Twain"),
                 AssistantMessage("Nice to meet you, Bark Twain!")]), "Chat not initialized correctly."

    with pytest.raises(TypeError):
        Chat([SystemMessage("You are a helpful assistant."), "This should fail."])


def test_call():
    """
    Test __call__ method.
    """
    # Expect ValueError if chat has no valid llm.
    chat_without_llm = Chat("You are a helpful assistant.")
    with pytest.raises(ValueError):
        chat_without_llm("My name is Bark Twain.")

    chat_with_wrong_llm = Chat("You are a helpful assistant.", llm=True)
    with pytest.raises(ValueError):
        chat_with_wrong_llm("My name is Bark Twain.")

    # Expect TypeError if message is not a str, Message or Sequence[str | Message | Directive].
    chat = Chat("You are a helpful assistant.", llm=FakeLLM())
    assert chat("My name is Bark Twain.")
    assert chat(UserMessage("My name is Bark Twain."))
    assert chat([UserMessage("My name is Bark Twain."), AssistantMessage("Nice to meet you, Bark Twain!")])

    with pytest.raises(TypeError):
        chat(1)

    # Test return value for list of messages (list[str]) without any directives
    snippet = chat(["My name is Bark Twain.", "I am a dog."])
    assert len(snippet) == 4, "Expected 4 messages in total."
    assert len([m for m in snippet if isinstance(m, AssistantMessage)]) == 2, \
        "Expected 2 assistant messages in snippet."

    # Test chat with user and assistant messages.
    snippet = chat(["My name is Rex", AssistantMessage("Nice to meet you, Bark Twain!"), UserMessage("I am a dog.")])
    assert isinstance(snippet[-1], AssistantMessage), "Expected last message to be an assistant message."
    assert snippet[-1] == chat[-1], "Expected last message to be the same as in chat."
    assert len(snippet) == 4, "Expected 4 messages in total."

    # Test chat with directive.
    snippet = chat(["My name is Rex", TestDirective(), UserMessage("I am a dog."), TestDirective()])
    assert len(snippet) == 4, "Expected 4 messages in total."
    assert isinstance(snippet[1], AssistantMessage), "Expected second message to be an assistant message."
    assert isinstance(snippet[3], AssistantMessage), "Expected fourth message to be an assistant message."


def test_invoke_with_directive(chat):
    """
    Test _invoke_with_directive method.
    """
    directive = TestDirective()

    # Create a message, embed it, and parse it with the test directive.
    _input = "My name is Bark Twain."
    message = UserMessage(_input)

    # Test that the message is piped through the directive correctly.
    chat.append(message)
    assert chat[-1].text == message.text

    assistant_message = chat._invoke_with_directive(directive)
    assert chat[-1] == assistant_message, "Message not appended correctly."

    # Assert user message was updated correctly.
    assert message.text == directive.embed(_input)[0], \
        "Message not embedded correctly."
    assert chat[-2].text == message.text, \
        "Message not embedded correctly."
    assert chat[-2].info["original"] == _input, \
        "Original message not passed correctly."

    # Assert assistant message (response) was updated correctly.
    assert assistant_message.text == directive.parse(f"DUMMY RESPONSE for '{directive.embed(_input)[0]}'")[0], \
        "Message not parsed correctly."
    assert directive is assistant_message.info["directive"], \
        "Directive not passed correctly."
    assert assistant_message.info["original"] == f"DUMMY RESPONSE for '{directive.embed(_input)[0]}'", \
        "Original message not passed correctly."


def test_setitem(chat):
    """
    Test modified __setitem__ method.
    """
    # Test message type
    with pytest.raises(TypeError):
        chat[0] = "This should fail."

    # Test index
    message = SystemMessage("This should work.")
    chat[0] = message
    assert chat[0] is message, "Message not set correctly."

    message = SystemMessage("This should also work.")
    chat[-1] = message
    assert chat[-1] == message, "Message not set correctly."

    with pytest.raises(IndexError):
        chat[1] = SystemMessage("This should fail.")

    with pytest.raises(IndexError):
        chat[-2] = SystemMessage("This should also fail.")


def test_add_op(chat):
    """
    Test modified __add__ method.
    """
    assert chat + chat == Chat([*chat, *chat]), "Chats not added correctly."

    message = UserMessage("This should work.")
    assert chat + [message] == Chat([*chat, message]), \
        "Chat and list of messages not added correctly."

    with pytest.raises(TypeError):
        chat + ["This should fail."]

    with pytest.raises(TypeError):
        chat + SystemMessage("This should also fail.")

    with pytest.raises(TypeError):
        chat + "This should fail too."


def test_append(chat):
    """
    Test modified append method.
    """
    message = SystemMessage("This should work.")
    chat.append(message)
    assert chat[1] is message, "Message not appended correctly."

    with pytest.raises(TypeError):
        chat.append("This should fail.")


def test_extend(chat):
    """
    Test modified extend method.
    """
    messages = [UserMessage("My name is Bark Twain."), AssistantMessage("Hello, Bark Twain.")]
    chat.extend(messages)
    assert len(chat) == 3, "Messages not extended correctly."
    assert chat[1:] == messages, "Messages not extended correctly."

    with pytest.raises(TypeError):
        chat.extend("This should fail.")

    with pytest.raises(TypeError):
        chat.extend(["This should also fail."])


def test_insert(chat):
    """
    Test modified insert method.
    """
    message = SystemMessage("This should work.")
    chat.insert(0, message)
    assert chat[0] is message, "Message not inserted correctly."

    with pytest.raises(TypeError):
        chat.insert(0, "This should fail.")


def test_sort(chat):
    """
    Ensure that sort is not implemented.
    Should never be implemented, because it doesn't make for a chat.
    """
    with pytest.raises(NotImplementedError):
        chat.sort()


def test_validate(chat):
    """
    Test validate method.
    """
    chat.clear()
    assert chat.validate(), "Chat not validated correctly."

    system_message = SystemMessage("This is a system message.")
    user_message = UserMessage("This is a user message.")
    assistant_message = AssistantMessage("This is an assistant message.")

    chat.append(user_message)
    chat.append(assistant_message)

    # Test that chat is not validated if does not start with system message.
    with pytest.raises(ValueError):
        chat.validate()

    chat.insert(0, system_message)
    assert chat.validate(), "Chat not validated correctly."

    # Test that chat is not validated if messages are not alternating between user and assistant.
    chat.insert(2, user_message)
    with pytest.raises(ValueError):
        chat.validate()
    chat.pop(2)
    assert chat.validate(), "Chat not validated correctly."


def test_assert_all_messages(chat):
    """
    Test _assert_all_messages method.
    """
    messages = [UserMessage("My name is Bark Twain."), AssistantMessage("Hello, Bark Twain.")]
    assert chat._assert_all_messages(messages) is None, "Messages not validated correctly."

    with pytest.raises(TypeError):
        chat._assert_all_messages("This should fail.")

    with pytest.raises(TypeError):
        chat._assert_all_messages([SystemMessage("This should fail."), "This should also fail."])
