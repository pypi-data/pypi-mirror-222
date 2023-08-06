"""
This module contains Chat class, which is a subclass of list
and can be used to manage a conversation with a LLM.
"""

from collections.abc import Sequence
from typing import SupportsIndex

from lobsang.directives import Directive, TextDirective
from lobsang.llms.base import LLM
from lobsang.messages import Message, SystemMessage, UserMessage, AssistantMessage


class Chat(list[Message]):
    """
    A chat (subclass of list) holds a conversation between a user and an assistant. Each subsequent call of a chat
    instance with a message, i.e. `chat(message)`, will
        1. append the message,
        2. send it and the chat history (the message context) to the LLM and
        3. append the response to the chat as well

    >>> # It's a list everyone! 🎉
    >>> chat = Chat("You are a helpful assistant.")
    >>> len(chat)
    1
    >>> message = chat[0]
    >>> isinstance(message, SystemMessage)
    True
    >>> message.text
    'You are a helpful assistant.'
    """

    def __init__(self, data: str | Message | Sequence[Message] = (), llm: LLM = None):
        """
        Creates a new chat instance.

        **Note**: The message(s) you provide won't be sent to the LLM until you call the chat using the `__call__`
        method with a message. This setup allows you to define initial messages such as instructions and examples
        before starting the actual conversation.

        >>> # 1. Option: No parameters -> empty chat
        >>> chat = Chat()
        >>> len(chat)
        0
        >>>
        >>> # 2. Option: A string -> chat with a SystemMessage
        >>> chat = Chat("Hello World")
        >>> isinstance(chat[0], SystemMessage)
        True
        >>> chat[0].text
        'Hello World'
        >>>
        >>> # 3. Option: A Message -> chat with a Message (usually a SystemMessage to instruct the LLM)
        >>> chat = Chat(SystemMessage("Hello World"))
        >>> isinstance(chat[0], SystemMessage)
        True
        >>> chat[0].text
        'Hello World'
        >>>
        >>> # 4. Option: A list of messages -> chat with the provided messages
        >>> chat = Chat([SystemMessage("You are a helpful assistant."), UserMessage("My name is Bark Twain"),
        ... AssistantMessage("Nice to meet you, Bark Twain!")])
        >>> len(chat)
        3

        :param data: The message(s) to initialize the chat.
        :param llm: The language model to use. Currently, only OpenAI's API is supported.
        :raises TypeError: If data is not of type str, Message or Sequence[Message].
        """
        if isinstance(data, (str, Message)):
            data = [SystemMessage(data)] if isinstance(data, str) else [data]
        elif isinstance(data, Sequence):
            self._assert_all_messages(data)
        else:
            raise TypeError(f"Expected str, Message or Sequence[Message], got {type(data)} instead.")

        super().__init__(data)
        # If debug log level warn if llm is not set
        self.llm = llm

    def __call__(self, data: str | Message | Sequence[str | Message | Directive]) -> list[Message]:
        """
        Calls the chat with a message or a list of message(s) and returns the response(s) from the LLM.
        All messages (more accurately all directives) are sent to the LLM one by one in the order they are provided.

        >>> from lobsang.llms import FakeLLM
        >>> chat = Chat("You are a helpful assistant.", llm=FakeLLM())
        >>> len(chat)
        1
        >>> res = chat("My name is Bark Twain")
        >>> res[1].text
        "DUMMY RESPONSE for 'My name is Bark Twain'"
        >>> len(chat)
        3
        >>> res = chat(["What is 1+1?", "What is 2+2?"])
        >>> res[1].text
        "DUMMY RESPONSE for 'What is 1+1?'"
        >>> res[3].text
        "DUMMY RESPONSE for 'What is 2+2?'"

        :param data: The message(s) to send to the LLM.
        :return: The corresponding chat snippet, i.e. the message(s) you provided and the response(s) from the LLM.
        :raises ValueError: If no LLM set.
        :raises TypeError: If data is not of type str, Message or Sequence[Message | Directive].
        """
        # Ensure that an LLM is set
        if not isinstance(self.llm, LLM):
            raise ValueError("No LLM set. Please set self.llm to an instance of an LLM (e.g. 'Chat(llm=OpenAI())')")

        # If data is a string or a Message, convert it to a list of messages
        if isinstance(data, (str, Message)):
            data = [data]

        # Convert all strings to UserMessages
        data = [UserMessage(item) if isinstance(item, str) else item for item in data]
        self._assert_all_messages(data, allowed_types=(Message, Directive))

        # Insert default directive (TextDirective) after all messages, which are not followed by a directive. This
        # is necessary as the LLM is called on directives and not on messages. So we need a corresponding directive for
        # each message. For example the list [user_msg, user_msg, directive, user_msg] would be converted to
        # [user_msg, TextDirective, user_msg, directive, user_msg, TextDirective] (i.e. 2 TextDirectives are inserted).
        *rest, last = data
        for i, item in enumerate(rest):
            if isinstance(item, UserMessage) and not isinstance(data[i + 1], (AssistantMessage, Directive)):
                data.insert(i + 1, TextDirective())
        else:
            # Handle last message, which would raise an IndexError if handled in the loop
            if isinstance(last, UserMessage):
                data.append(TextDirective())

        # Loop through data, add non-directives to chat and send directives to LLM
        for item in data:
            if isinstance(item, Message):
                self.append(item)
            elif isinstance(item, Directive):
                self._invoke_with_directive(item)
            else:
                raise TypeError(f"Expected Message or Directive, got {type(item)} instead.")

        # Return response(s)
        return self[-len(data):]

    def _invoke_with_directive(self, directive: Directive) -> AssistantMessage:
        """
        Invokes the LLM with a directive.

        The provided directive is applied to the last message in the chat. The LLM then processes the chat history
        including the last message (the query). The response is parsed using the directive and appended to the chat.
        **Caution:** This method is not idempotent, i.e. it will change the chat history.

        :param directive: The directive to invoke the LLM with.
        :return: The response from the LLM as an AssistantMessage (also appended to the chat) for convenience.
        :raises TypeError: If the last message in the chat is not a UserMessage.
        """
        query = self[-1]

        if not isinstance(query, UserMessage):
            raise TypeError(f"Expected UserMessage, got {type(query)} instead.")

        # Update query with directive (embed instructions into text, update info)
        query.text, directive_info = directive.embed(query.text)
        query.info.update(directive_info)

        # Invoke LLM with chat as context
        response, llm_info = self.llm.chat(self)

        # Parse response
        parsed_response, directive_info = directive.parse(response)

        # Create AssistantMessage
        assistant_info = llm_info | directive_info | {'directive': directive, 'query': query}
        assistant_message = AssistantMessage(parsed_response, info=assistant_info)

        self.append(assistant_message)
        return assistant_message

    def __setitem__(self, __i: SupportsIndex, __o: Message) -> None:
        """
        Sets an item at a given index in the chat.

        :param __i: The index to set the message at.
        :param __o: The message to set.
        :raises IndexError: If __i is out of range.
        :raises TypeError: If __o is not of type Message.
        """
        if not isinstance(__o, Message):
            raise TypeError(f"Expected Message, got {type(__o)} instead.")

        super().__setitem__(__i, __o)

    def __add__(self, other: Sequence[Message]):
        """
        Concatenates two chats using the + operator.

        >>> chat = Chat("You are a helpful assistant.")
        >>> messages = [UserMessage("My name is Bark Twain"), AssistantMessage("Nice to meet you, Bark Twain!")]
        >>> chat + messages == chat.__add__(messages) == Chat([*chat, *messages])
        True

        :param other: A sequence of messages to concatenate with the chat.
        :return: A new chat containing the messages of both chats.
        :raises TypeError:  If other is not of type Sequence[Message].
        """
        return Chat([*self, *other])

    def append(self, __object: Message) -> None:
        """
        Appends a message to the chat.

        :param __object: The message to append.
        :raises TypeError: If __object is not of type Message.
        """
        if not isinstance(__object, Message):
            raise TypeError(f"Expected Message, got {type(__object)} instead.")

        super().append(__object)

    def extend(self, sequence: Sequence[Message]) -> None:
        """
        Extends the list by appending all items from the sequence.
        :param sequence: The messages to extend the chat with.
        :raises TypeError: If sequence is not of type sequence[Message].
        """
        if not isinstance(sequence, Sequence):
            raise TypeError(f"Expected a sequence of Messages, but got {type(sequence)} instead.")

        self._assert_all_messages(sequence)
        super().extend(sequence)

    def insert(self, __index: SupportsIndex, __object: Message) -> None:
        """
        Inserts a message at a given index into the chat history.

        :param __index: The index to insert the message at.
        :param __object: The message to insert.
        :raises TypeError: If __object is not of type Message.
        """
        if not isinstance(__object, Message):
            raise TypeError(f"Expected Message, got {type(__object)} instead.")

        super().insert(__index, __object)

    def sort(self, *args, **kwargs):
        raise NotImplementedError("Alas, the mystical art of sorting remains a secret yet to be unlocked "
                                  "in this enchanted realm of code. 🧙‍♂️")

    def validate(self):
        """
        Validates the chat according to the following rules:
        1. The chat must start with a SystemMessage
        2. Messages after the first message must alternate between UserMessage and AssistantMessage,
        starting with a UserMessage.

        :return: True if the chat is valid, otherwise raises a ValueError.
        :raises ValueError: If the chat is not valid.
        """
        if not self:
            return True

        if not isinstance(self[0], SystemMessage):
            raise ValueError(f"Expected the first message to be a SystemMessage, but got {type(self[0])} instead.")

        for i, message in enumerate(self[1:], start=0):
            if i % 2 == 0 and not isinstance(message, UserMessage):
                raise ValueError(f"Expected a UserMessage at index {i}, but got {type(message)} instead.")
            elif i % 2 == 1 and not isinstance(message, AssistantMessage):
                raise ValueError(f"Expected a AssistantMessage at index {i}, "
                                 f"but got {type(message)} instead.")

        return True

    @staticmethod
    def _assert_all_messages(sequence: Sequence, allowed_types=(Message,)):
        """
        Asserts that all items in the sequence are of one of the allowed types.

        :param sequence: The sequence to assert.
        :param allowed_types: The allowed types.
        :raises TypeError: If sequence contains items that are not of one of the allowed types.
        """
        invalid_items = [(i, item, type(item)) for i, item in enumerate(sequence) if
                         not isinstance(item, allowed_types)]
        if invalid_items:
            raise TypeError(
                f"Expected items of type Message, but got {len(invalid_items)} invalid items:\n{invalid_items}")

    def __str__(self):
        return str([*map(str, self)])

    def __repr__(self):
        # Show only the first and last two messages if the chat is longer than 4 messages
        excerpt = [*map(str, self[:2]), "...", *map(str, self[-2:])] if len(self) > 4 else [*map(str, self)]

        return f"Chat(llm={self.llm.__class__.__name__ if isinstance(self.llm, LLM) else self.llm}, " \
               f"total_messages={len(self)}), messages={excerpt}"