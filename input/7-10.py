
lugares = []
pesquisa = True

while pesquisa:
    resposta = input("Qual lugar voce gostaria de visitar:? ")
    lugares.append(resposta)
    repeat = input("Gostaria de adicionar mais lugares? (yes/no)")
    if repeat == 'no':
        pesquisa = False

print("Resultados\n")
print("Os lugares que voce gostaria de visitar sao: ")
for lugar in lugares:
    print(f"{lugar.title()}")
    
    