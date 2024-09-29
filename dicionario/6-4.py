
"""
6.4 – Glossario 2: Agora que você já sabe como percorrer um dicionário com um 
laço, limpe o codigo do exercicio 6.3 (página 155), substituindo suas series de
instruções print por um laço que percorra o dicionário e exiba cada chave e seu
valor. Quando tiver certeza de que seu laço funciona, adicione cinco termos
relacionados à programação que você acabou de aprender.
"""

glossario = {
    'print': 'Imprime uma mensagem na tela.',
    'input': 'Recebe uma mensagem do usuário.',
    'if': 'Testa uma condição.',
    'else': 'Caso a condição seja falsa.',
    'for': 'Laço de repetição',
}

print("As palavras e seus significados são:\n")
for palavra, significado in glossario.items():
    print(f"{palavra}: {significado}\n")