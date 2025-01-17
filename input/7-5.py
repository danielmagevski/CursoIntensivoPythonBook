
"""
7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para diferentes
grupos etários. Se uma pessoa tiver menos de 3 anos, o ingresso será gratuito; se
tiver entre 3 e 12 anos, o ingresso custará 10 dólares; se tiver mais de 12 anos, o
ingresso custará 15 dólares. Escreva um laço em que você pergunte a idade dos
espectadores e, então, informe o preço do ingresso.  
"""

idade = int(input("Qual a idade do espectador? "))

while idade >= 0:
    if idade < 3:
        print("O ingresso é gratuito.")
    elif idade >= 3 and idade <= 12:
        print("O ingresso custa $10.")
    elif idade > 12:
        print("O ingresso custa $15.")
    idade = int(input("Qual a idade do espectador? "))
