
"""
5.9 – Sem usuários: Acrescente um teste if em user.py para garantir que a lista 
de usuários não esteja vazia.
- Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns 
usuários!
- Remova todos os nomes de usuários da lista e certifique-se de que a mensagem
correta seja exibida.
"""

users = ["daniel"]

if users:
    for user in users:
        print(f"Ola {user}, obrigado por fazer login novamente.")
else:
    print("E necessario encontrar alguns usuarios!")