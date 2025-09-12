"""
8.12 – Sanduiches: Crie uma funcao que aceite uma lista de itens que uma pessoa
quer em sanduiche. A funcao deve ter um paramentro que colete todos os itens
forneceidos na chamada de funcao e deve exibir um resumo do sanduiche que esta
sendo solicitado. Chame a funcao tres vezes, com um numero diferente de
argumentos a cada vez.
"""

def build_sanduich(*args):
    print(args)

sanduiche1 = build_sanduich("carne", "queijo", "tomate")
sanduiche2 = build_sanduich("frango", "alface")
sanduiche3 = build_sanduich("atum", "maionese", "cebola roxa", "picles")
