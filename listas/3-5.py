"""
3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print no
final de seu programa, especificando o nome do convidado que não poderá
comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista.
"""
convidados = ['João', 'Maria', 'José']
msg = 'Olá, gostaria de convidar você para jantar'

# Exibe as mensagens de convite originais
print(msg + ', ' + convidados[0])
print(msg + ', ' + convidados[1])
print(msg + ', ' + convidados[2])

# Especificando o nome do convidado que não poderá comparecer
nao_pode_comparecer = 'Maria'
print(f'\nInfelizmente, {nao_pode_comparecer} não poderá comparecer ao jantar.\n')

# Modificando a lista, substituindo o nome do convidado que não poderá comparecer
novo_convidado = 'Ana'
convidados[convidados.index(nao_pode_comparecer)] = novo_convidado

# Exibe o segundo conjunto de mensagens com o novo convidado
print('Novo conjunto de convites:')
print(msg + ', ' + convidados[0])
print(msg + ', ' + convidados[1])
print(msg + ', ' + convidados[2])

