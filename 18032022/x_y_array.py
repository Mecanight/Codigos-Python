# importando a biblioteca

import pandas as pd

#criar um dataframe

df = pd.DataFrame(
    {
        "coluna0":[854,26187,9318,961,5184,81218,7,2],
        "coluna1":[90,45,78,34,991,25,7,459],
        "coluna2":[99,46,45,78,78,368,12,73248],
        "coluna3":[100,456,234,1345,1212,457935,4587,8546],
        "coluna4":[19,528,35,2,10540,85,5,458],
        "coluna5":[78,85,36,2500,8,74563,852,1],
        "coluna6":[7589620,4,9,48,62,42698,45,74321],
        "coluna7":[5812,840,85842,5,82555,81792,6225,65],
        "coluna8":[57854,84,7,874,44776,955,8,548844],
        "coluna9":[8,845558,4771932,74136955,9,852,9235,9]
    }
)

print(df)
print("-----------------")
print("Sequencia das tabelas")
print("-----------------")
print(df.mean(axis = 0))
print("-----------------")
print("Sequencia das tabelas")
print("-----------------")
print(df.mean(axis = 1))
