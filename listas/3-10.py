"""
3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma lista.
Por exemplo, você poderia criar uma lista de montanhas, rios, países, cidades,
idiomas ou qualquer outro item que quiser. Escreva um programa que crie uma
lista contendo esses itens e então utilize cada função apresentada neste
capítulo pelo menos uma vez.
"""
rios = ['Amazonas', 'Nilo', 'Mississipi', 'Sena', 'Tâmisa']
pais = ['Brasil', 'Egito', 'Estados Unidos', 'França', 'Inglaterra']
carros = ['Fusca', 'Ferrari', 'Porsche', 'Lamborghini', 'Aston Martin']

len_rios = len(rios)
print(f'Número de rios que gostaria de conhecer: {len_rios}')

iniciais = [p[0] for p in pais]
print(f"Iniciais de cada país: {iniciais}")

