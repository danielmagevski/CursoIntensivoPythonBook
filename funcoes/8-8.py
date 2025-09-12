"""
8.8 – Album de usuarios: Comece com seu programa do Exercicio 8.7. Escreva um
loop while que possibilite aos usuarios inserir o artista e o titulo de um album.
Apos receber essas informacoes, chamem o make_album() com a entrada do usuario e
exiba o dicionario criado. Não se esqueça de incluir um valor de saida no loop
while.
"""

def make_album(artista, titulo):
    album = {'Artista': artista, 'Album': titulo}
    return album

while True:
    print("\nDigite 'q' a qualquer momento para sair.")

    artista = input("Coloque o nome do artista: ")
    if artista.lower() == 'q':
        break

    titulo = input("Coloque o título do álbum: ")
    if titulo.lower() == 'q':
        break

    album = make_album(artista, titulo)
    print(album)
