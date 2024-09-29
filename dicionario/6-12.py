
"""
6.12 – Extensões: Agora que já estamos trabalahndo com exemplos complexos o
suficiente para que sejam mas desenvolvidos de diferentes maneira, use um dos 
programas de exemplo desse capitulo e expanda-o. Por exemplo, adicione mais
informações sobre cada pessoa (como idade, cidade onde mora, etc.) ou mais
informações sobre cada cidade (como o clima, a economia, etc.).
"""

pessoa = {'first_name': 'Samuel', 'last_name': 'Costa', 'age': 30, 'city': 'Vitoria'}
pessoa2 = {'first_name': 'Jose', 'last_name': 'Silva', 'age': 25, 'city': 'Vila Velha'}
pessoa3 = {'first_name': 'Maria', 'last_name': 'Santos', 'age': 35, 'city': 'Vila Velha'}

pessoa['country'] = 'Brasil'
pessoa2['country'] = 'Brasil'
pessoa3['country'] = 'Brasil'

pessoas = [pessoa, pessoa2, pessoa3]

for pessoa in pessoas:
    print(f"Nome: {pessoa['first_name']} {pessoa['last_name']}")
    print(f"Idade: {pessoa['age']}")
    print(f"Cidade: {pessoa['city']}")
    print(f"País: {pessoa['country']}")
    print()