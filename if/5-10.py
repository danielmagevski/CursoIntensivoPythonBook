
"""
5.10 – Verificando nomes de usuários: Faça o seguinte para criar um programa que
simule como os sites garantem que todos tenham um nome de usuário único.
- Crie uma lista chamada current_users com cinco nomes de usuários.
- Crie outra lista chamada new_users com cinco outros nomes de usuários.
- Garanta que um ou dois dos novos nomes de usuários também estejam na lista
current_users.
"""


current_users = ["Admin", "user1", "user2", "user3", "user4"]
new_users = ["admin", "user5", "user6", "user7", "user8"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"O nome de usuario {new_user} ja esta em uso, por favor escolha outro.")
    else:
        print(f"O nome de usuario {new_user} esta disponivel.")
