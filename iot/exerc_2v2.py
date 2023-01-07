import RPi.GPIO as gpio
import time as delay

gpio.setmode(gpio.BOARD)

led_vermelho, led_verde, botao = 11, 12, 18
contador = 0

gpio.setup(led_vermelho, gpio.OUT)
gpio.setup(led_verde, gpio.OUT)
gpio.setup(botao, gpio.IN)

gpio.output(led_vermelho, False)
gpio.output(led_verde, False)

def pisca_leds():
    gpio.output(led_vermelho, True)
    gpio.output(led_verde, True)
    delay.sleep(0.5)
    gpio.output(led_vermelho, False)
    gpio.output(led_verde, False)
    delay.sleep(0.5)
while True:
    if gpio.input(botao) == True:
        contador = contador + 1
        delay.sleep(0.5)
        pisca_leds()
        print('Clique nº '+str(contador))
        if contador == 6:
            print('Sexto clique no botão, reiniciaremos o sistema')
            contador = 0