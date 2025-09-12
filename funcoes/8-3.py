"""
8.3 – Camiseta: Crie uma função chamada make_skirt() que aceita um tamanho e o 
texto que deve ser estampado na camiseta. A funcao deve exibir uma frase resumindo
o tamanho da camiseta e a mensagem estampada nela.
- Chame a função uma vez usando argumentos posicionais para criar a camiseta.
- Chame a função uma vez usando argumentos nomeados para criar a camiseta.
"""
def make_shirt(tamanho, texto):
    print(f"Camiseta é do tamanho {tamanho} e com texto {texto}")
    
make_shirt("G", "Ola")
make_shirt(tamanho = "G", texto="Ola")