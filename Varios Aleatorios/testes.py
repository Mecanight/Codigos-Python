"""print('Hello World')
nome = "Mecanight"
idade = 32
altura = 1.78
print(nome,'tem', idade, 'anos e', altura, "m de altura")
a = 4
b = 5
c = 6
soma = a + b + c
subtr = a - b - c
multip = a * b * c
divis = a / b / c
print(soma, subtr, multip, divis)
print((soma - subtr), (multip / divis ))
for i in range (1, 5):
    print('500', i)
    for j in range (1, 10):
        print('100', j)
def soma_um(idade):
    print('Tá dentro da função')
    return idade + 1
idade  = 32
for i in range(1, 10):
    print(soma_um(idade + i))
print('Fora da função')
print(soma_um(50))
print(input("Digite a temperatura em ºC"))
cels = input
def converte_celsius_em_fahrenheit(cels):
    fahr = cels * 1.8 + 32
    return fahr
print(cels,"º C são",converte_celsius_em_fahrenheit(32),"º F")
print('56 ºC são',converte_celsius_em_fahrenheit(56),'ºF')

def converte_celsius_em_kelvin(cels):
    kelv = cels - 273,15
    return kelv
print('32º C são',converte_celsius_em_kelvin(32),'º K')
print('56 ºC são',converte_celsius_em_kelvin(56),'º K')

def converte_kelvin_em_fahrenheit(kelvin):
    cels =  kelvin + 273.15
    fahre = converte_celsius_em_fahrenheit(kelvin)
    return fahre
print(converte_kelvin_em_fahrenheit(-270))
print("Iniciando")
x = 5
y = 18
if(x>y):
    print("X É maior")
else:
    print("Y É o maior")

x = 20
y = 18
if(x>y):
    print("X É maior")
else:
    print("Y É o maior")"""


lista_numeros = [45, 55, 65, 75, 85, 95]

def imprimir_numeros(numeros_pra_imprimir):
    print("A lista de numeros para imprimir")
    for item in numeros_pra_imprimir:
        print(item)
imprimir_numeros(lista_numeros)