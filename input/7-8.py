
"""
7.8 – Lanchonete: Crie uma lista chamada sanduiches_orders e preencha-a com os
nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada 
finished_sandwiches. Percorra a lista sanduiches_orders com um laço e, 
para cada sanduíche.
Dentro do laço, exiba uma mensagem informando que você está trabalhando com o
sanduíche e o transfira para a lista de sanduíches prontos. Depois que todos os
sanduíches estiverem prontos, exiba uma mensagem que liste cada sanduíche
preparado.

"""

sandwitch_orders = ['atum', 'carne', 'frango']

finished_sandwiches = []

while sandwitch_orders:
    currents_orders = sandwitch_orders.pop()
    
    print(f"Seu lanche de {currents_orders.title()} esta pronto")
    finished_sandwiches.append(currents_orders)
    
print("\nA lista do seu lanche")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
    
    
    