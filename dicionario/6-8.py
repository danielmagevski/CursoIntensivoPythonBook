
"""
6.8 – Animais de estimação: Crie varios dicionários, em que o nome de cada 
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o
tipo do animal e o dono. Armazene esses dicionários em uma lista chamada pets.
Em seguida, percorra sua lista com um laço e, à medida que fizer isso, apresente
tudo que você sabe sobre cada animal de estimação.
"""

animal1 = {'nome': 'Rex', 'especie': 'cachorro', 'raca': 'poodle'}
amimal2 = {'nome': 'Mimi', 'especie': 'gato', 'raca': 'siames'}
amimal3 = {'nome': 'Pé de Pano', 'especie': 'cavalo', 'raca': 'puro sangue'}

pets = [animal1, amimal2, amimal3]

for pet in pets:
    print('Nome:', pet['nome'])
    print('Especie:', pet['especie'])
    print('Raca:', pet['raca'])
    print()