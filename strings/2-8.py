"""
2.8 – O Python tem um método removesuffix() que funciona exatamente como 
removeprefix(). Atribua o valor de  'python_notes.txt' a uma variavel chamada
filename. Depois, utilize o método removesuffix() para exibir o nome do arquivo
sem a extensão do arquivo, como alguns navegadores de arquivos fazem.
"""

filename = "python_notes.txt"

print(filename.removesuffix(".txt"))