
"""
5.11 – Numeros ordinais: Os numeros ordinais designam sua posicao em uma lista,
como 1st ou 2nd. A Maioria dos numeros ordinais em ingles termina com th, exceto
1,2 e 3.
"""

numeros = [n for n in range(1, 11)]
for n in numeros:
    if n == 1:
        print('1st')
    elif n == 2:
        print('2nd')
    elif n ==3:
        print('3rd')
    else:    
        print(f'{n}th')
