import RPi.GPIO as gpio
import time as delay

gpio.setmode(gpio.BOARD)

led_vermelho = 11
led_verde = 12
contador_vermelho = 0
contador_verde = 0

gpio.setup(led_vermelho, gpio.OUT)
gpio.setup(led_verde, gpio.OUT)

while True:
    gpio.output(led_vermelho, True)
    contador_vermelho += 1
    print('Led Vermelho ON')
    print(contador_vermelho)
    delay.sleep(0.5)
    gpio.output(led_vermelho, False)
    delay.sleep(0.5)
    gpio.output(led_verde, True)
    contador_verde += 1
    print('Led Verde ON')
    print(contador_verde)
    delay.sleep(0.5)
    gpio.output(led_verde, False)
    delay.sleep(0.5)