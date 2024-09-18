"""
3.8 - Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você 
gostaria de visitar.
• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja
em ordem alfabética.
• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
elegante; basta exibi-la como uma lista Python pura.
• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a
lista propriamente dita.
• Mostre que sua lista manteve sua ordem original exibindo-a.
• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar
a ordem da lista original.
• Mostre que sua lista manteve sua ordem original exibindo-a novamente.
• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
que sua ordem mudou.
• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista
para mostrar que ela voltou à sua ordem original.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem
alfabética. Exiba a lista para mostrar que sua ordem mudou.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem
alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.
"""

lugares = ["Tóquio", "Nova York", "Paris", "Londres", "Sydney"]

print("Lista original:")
print(lugares)
print("\nLista em ordem alfabética (usando sorted()):")
print(sorted(lugares))
print("\nLista original após sorted():")
print(lugares)
print("\nLista em ordem alfabética inversa (usando sorted() com reverse=True):")
print(sorted(lugares, reverse=True))
print("\nLista original após sorted() com reverse=True:")
print(lugares)
lugares.reverse()
print("\nLista após usar reverse():")
print(lugares)
lugares.reverse()
print("\nLista após usar reverse() novamente:")
print(lugares)
lugares.sort()
print("\nLista após usar sort() em ordem alfabética:")
print(lugares)
lugares.sort(reverse=True)
print("\nLista após usar sort() em ordem alfabética inversa:")
print(lugares)
