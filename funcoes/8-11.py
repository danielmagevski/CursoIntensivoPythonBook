"""
8.11 – Mensagem arquivadas: Comece sua tafera a partir do exercicio 8.10. Chame
a funcao send_messaes() com uma copia da lista de mensagens. Após chamar a funcao,
exiba ambas as listas para mostrar que a lista original reteve suas mensagens
"""

def send_messages(messages, sent_messages):
    """Exibe cada mensagem e copia para a lista de mensagens enviadas."""
    for message in messages:
        print(f"Enviando mensagem: {message}")
        sent_messages.append(message)

messages = ["Olá", "Como você está?", "Tenha um ótimo dia!"]
sent_messages = []


send_messages(messages, sent_messages)


print("\nMensagens originais:", messages)
print("Mensagens enviadas:", sent_messages)