import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

led_vermelho, led_verde, botao = 11, 12, 18
contador = 0
i = 0

gpio.setup(led_vermelho, gpio.OUT)
gpio.setup(led_verde, gpio.OUT)
gpio.setup(botao, gpio.IN)

gpio.output(led_vermelho, False)
gpio.output(led_verde, False)

def pisca_led_vermelho():
    gpio.output(led_vermelho, True)
    delay.sleep(0.5)
    gpio.output(led_vermelho, False)
    delay.sleep(0.5)
    
def pisca_led_verde():
    gpio.output(led_verde, True)
    delay.sleep(0.5)
    gpio.output(led_verde, False)
    delay.sleep(0.5)
    
def piscar_ambos():
    gpio.output(led_vermelho, True)
    gpio.output(led_verde, True)
    delay.sleep(0.5)
    gpio.output(led_verde, False)
    gpio.output(led_verde, False)
    delay.sleep(0.5)

while True:
    if gpio.input(botao) == True:
        contador = contador + 1
        delay.sleep(0.5)
        ptint('Clique número: ', str(contador))
        if contador == 1:
            pisca_led_vermelho()
            pisca_led_vermelho()
            pisca_led_vermelho()
            pisca_led_vermelho()
            pisca_led_vermelho()
            i += 1
        if contador == 2:
            pisca_led_verde()
            pisca_led_verde()
            pisca_led_verde()
            pisca_led_verde()
            pisca_led_verde()
        if contador == 3:
            piscar_ambos()
            piscar_ambos()
            piscar_ambos()
            piscar_ambos()
            piscar_ambos()
        if contador == 4:
            print('Quarto clique no botão, ao clicar novamente reinicia o sistema')
        if contador == 5:
            contador = 0
            print('Processo reiniciado')