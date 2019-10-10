# coding=utf-8
# !/usr/bin/python3
from __future__ import unicode_literals
import paho.mqtt.client as mqtt
import time
clientid = "server_buzzer"
username = 'jiangtianting'
password = '1234'
client = mqtt.Client(clientid)
beep_dic={"server_buzzer":"beep","server_buzzer1":"beep1"}


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("device_alert")


def on_message(client, userdata, msg):
    print(msg.topic + " " + bytes.decode(msg.payload))
    t1 = eval(bytes.decode(msg.payload))
    device_status = t1['status']
    if device_status == "1":
        beep_id=t1['deviceId']
        beep_ring=str(beep_dic[beep_id])
        print(type(beep_ring),beep_ring)
        ring=__import__(beep_ring)
        ring.main()
    else:
        pass


def on_publish(topic, payload, qos):
    client.publish(topic, payload, qos)



def main():
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username, password)
    client.connect("192.168.0.40", 1883, 600)
    client.loop_forever()


if __name__ == '__main__':
    main()
