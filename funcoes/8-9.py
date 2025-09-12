"""
8.9 – Mensagens: Cria uma lista com uma serie de mensagens curtas e de texto.
"""

def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Hello", "How are you?", "Good morning", "Good night", "Have a great day!"]
show_messages(messages)