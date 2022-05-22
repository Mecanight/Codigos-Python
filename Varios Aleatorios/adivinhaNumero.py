import random

print("seja bem vindo")

#print(numero_a_ser_descoberto)

numero_a_ser_descoberto = random.randrange(1,101)
numero_de_tentativas = 0
tentativa = 1
numero_de_pontos = 1000

print("Dificuldade: ")
print("(1) Fácil | (2) Médio | (3) Hard")

dificuldade = int(input("Selecione um nível de dificuldade"))

if(dificuldade == 1):
    numero_de_tentativas = 15
elif(dificuldade == 2):
    numero_de_tentativas = 10
else:
    numero_de_tentativas = 5

while(tentativa <= numero_de_tentativas):
    print(f"Mermao, voce está na tentativa: {tentativa}, de um total de: {numero_tentativas}.")
    chute_string  = int(imput("Qual o chute (1 - 100): "))
    chute  = int(chute_string)
    
    if(chute < 1 or chute > 100):
        print("você não leu a minha mensagem. vergonha da profission")
        exit()
        
    acerto = chute == numero_a_ser_descoberto
    maior = chute > numero_a_ser_descoberto
    menor = chute < numero_a_ser_descoberto

    print(f"Mano, voce chutou o numero: {chute}")

    if(acerto):
        print(f"Parabéns! você nao eh burro! voce fez: {numero_de_pontos} pontos")
        break
    else:
        if(maior):
            print("voce chutou um numero maior do que o sorteado")
        elif(menor):
            print("voce chutou um numero menor do que o sorteado")
        pontos_perdidos = 15
        numero_de_pontos -= numero_perdidos
        #numero_de_pontos = numero_de_pontos - pontos_perdidos

    tentativa += 1
print(f"Fim de jogo! o numero sorteado era: {numero_a_ser_descoberto}")
