
"""
7.2 – Reservas de restaurante: Crie um programa que pergunte quantos lugares em
uma mesa o usuario precisa. Se a resposta for maior que 8, exiba uma mensagem
dizendo que a pessoa deverá esperar por uma mesa. Caso contrário, informe que a
mesa está pronta.
"""

mesa = input("Quantas pessoas estarão no seu grupo para jantar? ")
mesa = int(mesa)

if mesa > 8:
    print("Desculpe, você terá que esperar por uma mesa.")
else:
    print("Sua mesa está pronta.")