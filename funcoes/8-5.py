"""
8.5 – Cidades: Escreva uma funcão chamada describe_city() que aceite o nome de uma
cidade e de seu país. A função deve exibir uma frase, como "A cidade Rio de Janeiro
fica no Brasil". Forneça ao parâmetro país um valor padrão. Chame a funcao para três
cidades diferentes e, pelo menos para uma que não esteja no país padrão.
"""

def describe_city(cidade, pais="Brasil"):
    print(f"A cidade {cidade} fica no {pais}")
    
describe_city("Vitoria")
describe_city("Rio de Janeiro")
describe_city("Buenos Aires", "Argentina")
