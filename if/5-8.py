
"""
5.8 – Nomes de usuários: Faça uma lista de cinco ou mais nomes de usuários,
incluindo o nome 'admin'. Suponha que você esteja escrevendo um código que exibirá
uma saudação a cada usuário depois que ele fizer login em um site. Percorra a lista
com um laço e mostre uma saudação para cada usuário:
- Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo,
Olá admin, gostaria de ver um relatório de status?
- Caso contrário, mostre uma saudação genérica, por exemplo, Olá Usuario, obrigado
por fazer login novamente.
"""

users = ['admin', 'user1', 'user2', 'user3', 'user4']

for user in users:
    if user == 'admin':
        print(f"Ola {user}, gostaria de ver um relatorio de status ?")
    else:
        print(f"Ola {user}, obrigado por fazer login novamente.")