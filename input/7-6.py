
"""
7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do Exercício 
7.5 que execute pelo menos três vezes. Certifique-se de que uma das versões:
• Use um teste condicional na instrução while para encerrar o laço.
• Use uma variável active para controlar o tempo que o laço executará.
• Use uma instrução break para sair do laço quando o usuario informar um valor
"""

msg = "Digite os ingredientes para a pizza: "
ingredientes = input(msg)

while ingredientes:
    print(f"Adicionando {ingredientes} à pizza.")
    ingredientes = input("Digite os ingredientes para a pizza: ")
    if ingredientes == 'quit':
        break
    

