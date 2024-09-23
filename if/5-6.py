
"""
5.6 – Fases da vida: Escreva uma cadeia de instruções if-elif-else que determine
a fase da vida de uma pessoa. Defina uma idade para uma pessoa e então exiba a
mensagem apropriada.
- Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo que 
ela é um bebê.
- Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem 
dizendo que ela é uma criança.
- Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma mensagem
dizendo que ela é um(a) garoto(a).
- Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma mensagem
dizendo que ela é um(a) adolescente.
- Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma mensagem
dizendo que ela é um adulto.
- Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que ela é um
idoso.

"""

age = 30

if age < 2:
    print("Você é um bebê!")
elif age >= 2 and age < 4:
    print("Você é uma criança!")
elif age >= 4 and age < 13:
    print("Você é um(a) garoto(a)!")
elif age >= 13 and age < 20:
    print("Você é um(a) adolescente!")
elif age >= 20 and age < 65:
    print("Você é um adulto!")
else:
    print("Você é um idoso!")
    