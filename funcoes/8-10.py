"""
8.10 – Enviando mensagem: Comece com uma copia do seu programa do exericio 8.9.
Escreva uma funcao chamada send_messages() para exibir cada mensagem de texto
e passe cada mensagem para uma nova lista chamada sent_messages à medida que é exibida.
Após chamar a função, exiba ambas as listas para ter certeza de que as mensagens foram
corretamente transferidas.
"""

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Enviando mensagem: {current_message}")
        sent_messages.append(current_message)

messages = ["Olá", "Como você está?", "Tenha um ótimo dia!"]
sent_messages = []


send_messages(messages, sent_messages)

print("\nMensagens originais (depois de enviar):", messages)
print("Mensagens enviadas:", sent_messages)