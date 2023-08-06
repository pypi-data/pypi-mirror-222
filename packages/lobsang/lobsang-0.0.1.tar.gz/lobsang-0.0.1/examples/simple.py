"""
A simple example of how to use lobsang.
"""

# try to install openai make sure it works with python3.11
# todo
# import
# from lobsang import Chat
#
# >>> from lobsang.chat import Chat, UserMessage, AssistantMessage
# >>> # Some examples of how to use the chat with directives
# >>> # 1. A single message (string or Message object). For getting started quickly.
# >>> chat = Chat("You are a helpful assistant.")
# >>> response = chat("What is 1 + 1?")
# >>> # Internally this will be automatically resolved, and is the same as
# >>> #                  👇 A user message    +      👇  The default directive, which returns a text response
# >>> response = chat([UserMessage("What is 1 + 1?"), TextDirective()])
# >>>
# >>> # 2. Multiple directives embedded in conversation.
# >>> chat = Chat("You are a helpful assistant.")
# >>> messages = [
# ...     UserMessage("Hello, my name is Bark Twain."),
# ...     # 👇 You can also setup example responses with the AssistantMessage to instruct the LLM
# ...     AsssistantMessage("Nice to meet you Bark Twain."),
# ...     UserMessage("Hello, my name is Droolius Caesar."),
# ...     TextDirective(),
# ...     UserMessage("Hello, my name is Biscuit Barkington."),
# ...     TextDirective()
# ... ]
# >>> # Calling chat with the message will automatically resolve the directives one by one.
# >>> # Note that all responses are immediately appended to the chat history and can be accessed via chat[index].
# >>> # The history is sent to the LLM with each call as context. So for example, to resolve the last directive,
# >>> # the messages[0:4] will be sent to the LLM as they were added to the chat history.
# >>> # Finally, the chat returns a list of responses (one for each directive).
# >>> responses = chat(messages)