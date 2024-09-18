"""
4.11 – Minhas pizzas, suas pizzas: Comece com o seu programa do Exercício 4.1
Faça uma cópia da lista de pizzas e chame-a de friend_pizzas. Em seguida, siga
as etapas;
- Adicione uma nova pizza à lista original.
- Adicione uma pizza diferente à lista friend_pizzas.
- Prove que você tem duas listas separadas. Exiba a mensagem Minhas pizzas
favoritas são: . E, em seguida use um loop for para exibir a segunda lista.
Garanta que cada pizza nova esteja armazenada na lista adequada.
"""

pizzas = ['marguerita', 'calabresa', 'portuguesa']
friend_pizzas = pizzas[:]
pizzas.append('pepperoni')
friend_pizzas.append('quatro queijos')

print("Minhas pizzas favoritas são:")
for p in pizzas:
    print(p)

print("\nAs pizzas favoritas do meu amigo são:")
for fp in friend_pizzas:
    print(fp)
    