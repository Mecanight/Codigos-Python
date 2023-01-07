import paho.mqtt.client as mqtt
import time as delay

mqtt_msg = ''

client = mqtt.Client('acad-Cassiano')
client.connect('10.10.10.80', 1883, 60)

def grupos(client, userdata, flags, rc):
    print('Conectado com código: ', str(rc))
    client.subscribe('aula/3011/mqtt')
    
def mensagens(client, userdata, msg):
    global mqtt_msg
    if msg.topic == 'aula/3011/mqtt':
        mqtt_msg = str(msg.payload.decode('utf-8'))
        print(msg.topic+'   '+mqtt_msg)

client.on_connect = grupos
client.on_message = mensagens

client.loop_forever()
client.disconnect()