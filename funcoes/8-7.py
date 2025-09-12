"""
8.7 – Album: Escreva uma função chamada make_album que crie um dicionário representando
um album de musica. A função deve ter o  nome de um artista e o titulo do album,
e deve retornar um dicionario com essas informações. Utilize a funcao para criar
tres dicionarios representando diferentes albums. Exiba cada valor de retorno
para mostrar que os dicionarios estão armazenando adequadamente as informações
do album.
Use None para adicionar um parametro opcional que armazene o numero de musicas
em um album. Se a linha chamadora incluir um valor para o numero de musicas,
adcione esse valor ao dicionario. Se não, o dicionario deve conter apenas o nome do artista
e o titulo do album.
"""

def make_album(artista, album, num_musicas=None):
    if num_musicas:
        person = {'Artista': artista, 'Album': album, 'Numero de Musicas': num_musicas}
        print (person)
    else:    
        person = {'Artista': artista, 'Album': album}
        print(person)

    
make_album('metallica', 'ride the lightning')
make_album('beethoven', 'ninth symphony')
make_album('willie nelson', 'red-headed stranger', 10)
