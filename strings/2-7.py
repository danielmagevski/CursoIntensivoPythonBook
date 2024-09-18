"""
2.7 – Removendo nomes: Use uma variavl para representar o nome de uma pessoa e
inclua alguns caracteres de espaço em branco no inicio e no final do nome. 
Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
Em seguida, printe o nome usando cada uma das tres funcoes de remoção de espaços
lstrip(), rstrip() e strip().
"""

name = "\t daniel\n "
name = name.strip()
print(name)