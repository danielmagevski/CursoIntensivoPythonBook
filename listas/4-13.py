"""
4.13 – Buffet: Um restaurante com serviço de buffet oferece apenas cinco 
refeiçoes basicas. Pense em cinco pratos simples e armazene-os em uma tupla.
- Use um laço for para exibir cada prato oferecido pelo restaurante.
- Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
- O restaurante muda o cardápio, substituindo dois dos itens com pratos diferentes.
Adicione uma linha que reescreva a tupla e, depois, use um loop for para exibir
cada um dos elementos do cardápio reformulado.
"""

cardapio = ('arroz', 'feijao', 'macarrao', 'batata', 'carne')
for c in cardapio:
    print(c)
    
# cardapio[0] = 'arroz integral' # TypeError:

cardapio = ('arroz integral', 'feijao', 'macarrao', 'batata', 'hmaburguer')

print("Cardápio reformulado: ")
for c in cardapio:
    print(c)

    