
"""
6.5 – Rios: Crie um dicionário que contenha tres rios importantes e o pais que
cada rio corta. Um exemplo para cada par deve ser 'nilo': 'egito'.
-  Use um laço para exibir uma frase sobre cada rio, como O Nilo corre pelo Egito.
-  Use um laço para exibir o nome de cada rio incluido no dicionário.
-  Use um laço para exibir o nome de cada pais incluido no dicionário.
"""

rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'ganges': 'india',
    'mississipi': 'estados unidos',
    'yangtze': 'china',
}

for rio, pais in rios.items():
    print(f"O rio {rio.title()} corre pelo {pais.title()}.\n")
for rio in rios.keys():
    print(f"Rio: {rio.title()}\n")
for pais in rios.values():
    print(f"Pais: {pais.title()}\n")