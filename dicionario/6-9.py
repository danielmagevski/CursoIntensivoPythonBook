
"""
6.9 – Lugares favoritos: Crie um dicionário chamado lugares_favoritos. Pense em
nomes de tres pessoas que voce conhece e armazene um lugar favorito para cada uma.
Para deixar este exercicio mais interessante, pergunte a cada pessoa o lugar
favorito dela.
-  Percorra o dicionario com um laço e apresente o nome de cada pessoa e seu lugar
favorito.
"""

lugares_favoritos = {
    'jen': 'paris',
    'sarah': ['roma', 'paris'],
    'edward': ['rio', 'sao paulo',]
    
}
for name, lugares in lugares_favoritos.items():
    print(f"{name.title()} gosta dos seguintes lugares:")
    print(f"\t{lugares}")