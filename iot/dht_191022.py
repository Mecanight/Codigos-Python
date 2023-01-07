import RPi.GPIO as gpio
import time as delay
import Adafruit_DHT as dht
import os

gpio.setmode(gpio.BOARD)

pin_sensor = 4

dht_sensor = dht.DHT11

f = open('/home/pi/notebooks/dht11.txt', 'a+')
f.write('Data          Hora         Temperatura     Humidade\n')
f.close()

while True:
    umid, temp = dht.read(dht_sensor, pin_sensor)
    if umid is not None and temp is not None:
        f = open('/home/pi/notebooks/dht11.txt', 'a+')
        f.write("{0}      {1}     {2:0.1f}ºC          {3:0.1f}%\n"
            .format(delay.strftime('%m/%d/%y'),delay.strftime('%H:%M:%S'),temp,umid))
        f.close()
        print("Temperatura: {0:0.1f}ºC Umidade: {1:0.1f}%".format(temp,umid))
    else:
        f = open('/home/pi/notebooks/dht11.txt', 'a+')
        f.write('{0}      {1}     Falha ao ler os dados do sensor\n'
            .format(delay.strftime('%m/%d/%y'),delay.strftime('%H:%M:%S')))
        f.close()
        print("Falha na leitura")
    delay.sleep(4)