import paho.mqtt.client as mqtt
import ssl
import json
import random
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection")

def connect(ip, port, user, password):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.tls_set(ca_certs=None, certfile=None, keyfile=None,cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLS)
    client.username_pw_set(str(user), str(password))

    client.connect(str(ip), port, 60)
    return client

def sendto_broker(ip, port, user, password, topic, dt):

    client = connect(ip, port, user, password)
    data = json.dumps(dt)
    client.publish(str(topic), str(data))

def enable_sub(ip, port, user, password, topic):
    client = connect(ip, port, user, password)

    def on_message(client, userdata, message):
        msg = message.payload.decode("UTF-8")
        data = json.loads(msg) 
        if data is not None:
            readfrom_broker.dt[0] = data

    client.loop_start()
    client.subscribe(str(topic))
    client.on_message = on_message
    time.sleep(0.15)
    #client.loop_stop()
    
class readfrom_broker():
    dt = [0,]

    def receive():
        if readfrom_broker.dt[0] != 0:
            data = readfrom_broker.dt[0]
            readfrom_broker.dt[0] = 0
            return data

if __name__ == '__main__':
    enable_sub("45.119.83.12",8883,"amt","123456","AmtLight/amt/Pub/HCM.016.010.001")
    readfrom_broker.receive()