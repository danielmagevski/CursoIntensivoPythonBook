
"""
6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2. 
Para que cada pessoa possa ter mais de um número favorito. Em seguida, apresente
o nome de cada pessoa, juntamente com seus números favoritos.
"""

numero_favorito = {
    'joao': 7,
    'maria':[ 3, 5],
    'pedro': [5, 9],
    'ana': 9,
    'carlos': 1,
}

for name, numero in numero_favorito.items():
    print(f"{name.title()} gosta dos seguintes numeros:")
    print(f"\t{numero}")
    print()