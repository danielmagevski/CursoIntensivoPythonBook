"""
8.6 – Nome de cidades: Escreva uma funcao chamada city_country() que recebe o
nome de uma cidade e seu pais, A função deve retornar uma string formatada como esta:
"Sao Paulo, Brasil".
- Chame a função com pelo menos tres pares de cidade-pais e exiba os valores formatados
"""

def city_country(cidade, pais):
    return f"{cidade}, {pais}"

print(city_country("Sao Paulo", "Brasil"))
print(city_country("Buenos Aires", "Argentina"))
print(city_country("Paris", "França"))
