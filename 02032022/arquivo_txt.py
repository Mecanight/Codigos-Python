# import csv

# abrir o arquivo

# with open("lista.txt") as arquivo:
#     #print(type(arquivo))w
#     tabela = reader(arquivo, delimiter = ",")
#
#     next(tabela)
#     #pular uma linha
#     print("Os filmes são:")
#     for linha in tabela:
#         titulo = linha[0]
#         ano = linha[1]
#         n_oscar = linha[2]
#
#         print(f"O file{titulo}, lancado no ano {ano} venceu {n_oscar} oscars")
#         nota = input('Diga a nota ou um comentário do filme?')

arquivo = open("arquivo_txt.txt", 'w')
for i in range(0,10):
        frase = input('Diga algo')
        arquivo.write(frase+"\n")
arquivo.close
