
"""
7.4 – Ingredientes para pizza: Escreva um loop que solicite ao usuario uma serie
de ingredientes para uma pizza até que o valor 'quit' seja informado. À medida que
cada ingrediente é especificado, exiba uma mensagem informando que você está
adicionando esse ingrediente à pizza. 
"""

msg = "Digite os ingredientes para a pizza: "
ingredientes = input(msg)

while ingredientes != 'quit':
    print(f"Adicionando {ingredientes} à pizza.")
    ingredientes = input("Digite os ingredientes para a pizza: ")

