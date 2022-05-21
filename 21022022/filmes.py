import csv

# abrir o arquivo

with open("filmes.csv") as arquivo:
    #print(type(arquivo))
    tabela = csv.reader(arquivo, delimiter = ",")

    next(tabela)
    #pular uma linha

    for linha in tabela:
        titulo = linha[0]
        ano = linha[1]
        n_oscar = linha[2]

        print(f"O filme {titulo}, lancado no ano {ano} venceu {n_oscar} oscars")
