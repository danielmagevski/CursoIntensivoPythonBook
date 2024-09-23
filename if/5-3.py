"""
5.3 – Cores de alienigenas #1: Imagine que um alienigena acabou de ser abatido
em umjogo. Crie uma variável chamada alien_color e atribua-lhe um valor igual a
'verde', 'amarelo' ou 'vermelho'.
- Escreva uma instrução if para testar se a cor do alienigena é verde. Se for,
mostre uma mensagem informando que o jogador acabou de ganhar 5 pontos.
- Escreva uma versão desse programa que execute o bloco if e outro que falhe.
"""

alien_color = ["verde", "amarelo", "vermelho"]

if "verde" in alien_color:
    print("Você ganhou 5 pontos!")
    
if "verde" not in alien_color:
    print("Você ganhou 10 pontos!") # Não será impresso, pois a condição não é verdadeira
