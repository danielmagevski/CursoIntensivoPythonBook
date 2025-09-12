"""
8.14 – Carros: Crie uma função que armazena informacoes sobre um carro em um
dicionario. A funcao deve sempre receber um fabricante e um nome de modelo.
Em seguida, deve aceitar um numero arbitrario de argumentos nomeados.
Chame a funcao com as informacoes necessarias e dois outros pares nome-valor,
como uma cor ou um recurso opcional, sua funçao deve funcionar mais ou menos
assim:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Exiba o dicionario retornado para garantir que todas as informacoes foram 
armazenadas corretamente.
"""

def make_car(fabicante, modelo, **car_info):
    car_info['fabricante'] = fabicante
    car_info['modelo'] = modelo
    return car_info

car = make_car('Honda', 'Civic', cor='preta', ano='2020')
print(car)

    