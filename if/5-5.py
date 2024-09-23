
"""
5.5 – Cores de alienigenas #3: Converta sua sequencia if-else do exercício 5.4 
em uam seguencia de ef-elif-else.
- Se o alienigena for verde, mostre uma mensagem informando que o jogador ganhou
5 pontos.
- Se o alienigena for amarelo, mostre uma mensagem informando que o jogador 
ganhou 10 pontos.
- Se o alienigena for vermelho, mostre uma mensagem informando que o jogador
ganhou 15 pontos.
- Escreva três versões desse programa, garantindo que a mensagem apropriada
"""

alien = "verde"

if alien == "verde":
    print("Você ganhou 5 pontos!")
elif alien == "amarelo":
    print("Você ganhou 10 pontos!")
else:
    print("Você ganhou 15 pontos!")