import csv

with open ("lista.csv") as arquivo:
    tabela = csv.reader(arquivo, delimiter = ",")

    next(tabela)

    for coluna in tabela:
        nome = coluna[0]
        sobrenome = coluna[1]
        idade = coluna[2]
        altura =coluna[3]
        pais = coluna[4]

        print(f"O {nome} {sobrenome} tem {idade} anos, {altura} metros de altura e mora no(a) {pais}")
