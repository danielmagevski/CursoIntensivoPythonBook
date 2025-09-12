"""
8.4 – Camisetas grandes: Modifique a função make_shirt() para que as camisetas
seja grandes por padrão com a seguinte frase estampada: "Eu amo python". Escreva
uma camiseta grande e uma média com a mensagem padrão e uma camiseta de qualquer
tamanho com uma frase diferente.
"""

def make_shirt(tamanho="G", texto="Eu amo python"):
    print(f"Camiseta é do tamanho {tamanho} e com texto {texto}")
    
make_shirt()
make_shirt(tamanho="M", texto="Eu gosto de programar")

