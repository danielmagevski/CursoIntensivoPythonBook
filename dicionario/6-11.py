
"""
6.11 – Cidades: Crie um dicionário chamado cidades. Use os nomes de três 
cidades como chaves em seu dicionário. Crie um dicionário de informações sobre 
cada cidade e inclua o país em que a cidade está localizada, sua população 
aproximada e um fato sobre essa cidade. As chaves do dicionário de informações 
devem ser algo como país, população e fato. Apresente o nome de cada cidade e 
todas as informações que você armazenou sobre ela.
"""

cidades = {
    'sao paulo': {
        'pais': 'brasil',
        'populacao': 12_252_023,
        'fato': 'Maior cidade do Brasil'
    },s
    'new york': {
        'pais': 'estados unidos',
        'populacao': 8_336_817,
        'fato': 'Cidade mais populosa dos EUA'
    },
    'rio de janeiro': {
        'pais': 'brasil',
        'populacao': 6_747_815,
        'fato': 'Cidade maravilhosa'
    }
}

for cidade, info in cidades.items():
    print(f"{cidade.title()} tem as seguintes informações:")
    print(f"\tPaís: {info['pais'].title()}")
    print(f"\tPopulação: {info['populacao']}")
    print(f"\tFato: {info['fato']}")
    print()
    