
"""
6.6 – Enquete: Utilize o código em favorite_languages.py.
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem de
programação, incluindo algumas pessoas que já estão no dicionário e outras que
não estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já
tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por
responder. Se ainda não participaram da enquete, apresente uma mensagem
convidando-as a responder. 
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

pessoas = ['jen', 'sarah', 'edward', 'phil', 'jose', 'maria', 'joao']

for pessoa in pessoas:
    if pessoa in favorite_languages.keys():
        print(f"{pessoa.title()}, obrigado por participar da enquete!")
    else:
        print(f"{pessoa.title()}, por favor, participe da enquete!")
