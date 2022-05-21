
import numpy as np

print('Exercício 1')

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]]
            )

B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]]
            )

print('A =\n',A)

print('\nB =\n',B)

produto = A.dot(B)

print('\nA * B =\n', produto)

###############################################################

print('\nExercício 2')

for linha in A:
    soma_linha = np.sum(linha)
    print('Soma da linha {} = {}'.format(linha, soma_linha))

print()

for linha in A:
    sub_linha = linha[0]-linha[1]-linha[2]
    print('Subtração da linha {} = {}'.format(linha, sub_linha))

###############################################################

print('\nExercício 3')

transposta = np.transpose(A)

print('\nTransposta de A\n', transposta)
