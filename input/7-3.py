
"""
7.3 – Multiplos de dez: Solicite um número ao usuário e, em seguida, informe se
o número é múltiplo de 10 ou não. 
"""
numero = int(input("Digite um número: "))
if numero % 10 == 0:
    print(f"{numero} é múltiplo de 10.")
else:
    print(f"{numero} não é múltiplo de 10.")