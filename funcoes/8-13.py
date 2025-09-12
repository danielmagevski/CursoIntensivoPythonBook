"""
8.13 – Perfil de usuário: Crie uma função que construa um perfil de usuário.
A função deve aceitar um nome, um sobrenome e um número variável de informações
de usuário (como idade, localização, etc.). A função deve retornar um dicionário
com todas as informações do usuário.
"""

def build_profile(nome, sobrenome, **user_info):
    user_info['nome'] = nome
    user_info['sobrenome'] = sobrenome
    return user_info

user_profile = build_profile('Daniel', 'Magevski',  pais='Brasil')

print(user_profile)
    