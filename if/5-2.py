"""
5.2 – Mais testes condicionais: Gere, pelo menos, um resultado True ou False para
cada condição a seguir:.
- Testes com operadores de igualdade e de diferença com string.
- Testes usando a função lower().
- Testes numericos com operadores de igualdade e de diferença, maior e menor que,
maior ou igual que e menor ou igual a.
- Testes para averiguar se um valor consta em uma lista.
- Testes para averiguar se um valor não consta em uma lista.
"""

nome = "daniel"
print(nome == "daniel")

cidade = "VITORIA"
print (cidade.lower() == "vitoria")

age1 = "30"
age2 = "40"

print(age1 > age2)

print(int(age1) >= 20 and int(age2) <= 50)

nomes = ["daniel", "joao", "maria", "jose"]
print("daniel" in nomes)

carros = ["fiat", "ford", "chevrolet", "volkswagen"]
print("fiat" not in carros)
