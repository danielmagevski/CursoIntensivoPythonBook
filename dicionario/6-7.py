
"""
6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1.
Crie dois novos dicionários que representem pessoas diferentes e armazene os três
dicionários em uma lista chamada people. Percorra sua lista de pessoas com um laço.
À medida que percorrer a lista, apresente tudo que você sabe sobre cada pessoa.
"""

pessoa = {'first_name': 'Samuel', 'last_name': 'Costa', 'age': 30, 'city': 'Vitoria'}
pessoa2 = {'first_name': 'Jose', 'last_name': 'Silva', 'age': 25, 'city': 'Vila Velha'}
pessoa3 = {'first_name': 'Maria', 'last_name': 'Santos', 'age': 35, 'city': 'Vila Velha'}

pessoas = [pessoa, pessoa2, pessoa3]

for pessoa in pessoas:
    print(f"Nome: {pessoa['first_name']} {pessoa['last_name']}")
    print(f"Idade: {pessoa['age']}")
    print(f"Cidade: {pessoa['city']}")
    print()