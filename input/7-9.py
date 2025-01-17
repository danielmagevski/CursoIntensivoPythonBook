"""
7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes. Adicione
um código próximo ao final de seu programa para exibir uma mensagem informando
que a lanchonete está sem pastrami, e então use um laço while para remover todas
as ocorrências de 'pastrami' de sandwich_orders. Garanta que nenhum sanduíche
de 'pastrami' acabe em finished_sandwiches.
"""

sandwitch_orders = ['atum', 'carne', 'frango', 'pastrami', 'pastrami',
                    'pastrami']
finished_sandwiches = []

print("Desculpe, estamos sem pastrami no momento.")
while 'pastrami' in sandwitch_orders:
    sandwitch_orders.remove('pastrami')

while sandwitch_orders:
    currents_orders = sandwitch_orders.pop()
    
    print(f"Seu lanche de {currents_orders.title()} esta pronto")
    finished_sandwiches.append(currents_orders)
