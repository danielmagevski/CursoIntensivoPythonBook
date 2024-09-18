"""
4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo, 
acrescente várias linhas no final do programa que façam o seguinte: 
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma 
fatia para exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir 
três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para 
exibir os três últimos itens da lista.
"""

cubos = [numero**3 for numero in range(1, 11)]


print("Lista completa de cubos:", cubos)


print("Os três primeiros itens da lista são:", cubos[:3])


meio = len(cubos) // 2
print("Três itens do meio da lista são:", cubos[meio-1:meio+2])

print("Os três últimos itens da lista são:", cubos[-3:])
