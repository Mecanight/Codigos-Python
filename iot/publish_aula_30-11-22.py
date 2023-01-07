import paho.mqtt.client as mqtt
import time as delay

client = mqtt.Client('acad-Cassiano')
client.connect('10.10.10.80', 1883, 60)
while True:
    try:
        client.publish('aula/3011/mqtt', 'Acad-Cassiano')
        delay.sleep(20)
    except Exception as e:
        client.loop_stop()
        client.disconnect()
        print(e)
        delay.sleep(20)
