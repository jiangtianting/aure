# coding=utf-8
# !/usr/bin/python3
from __future__ import unicode_literals
import paho.mqtt.client as mqtt
import uuid
import subprocess
import json
a1,a2,a3,a4="server_wendu","server_atp","server_light","server_co2"
s1,s2,s3,s4="BMP180_1.py","co2_1.py","gy_30.py","gpio.py"
sensor_status={s1:1,s2:1,s3:1,s4:1}
clientid = "server_check"
username = 'jiangtianting'
password = '1234'
client = mqtt.Client(clientid)
def check_sensor_status():
    for i  in sensor_status.keys():
        sensor_out=subprocess.call("python /test/%s"%(i),shell=True)
        if sensor_out==0:
            print(i+" is ok")
        else:
            print(i + " is error")
            sensor_status[i]=0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(topic, payload, qos):
    client.publish(topic, payload, qos)

def data_sum():
    data1, data2, data3, data4 = {"sn": a1, "status": sensor_status[s4]}, \
                                 {"sn": a2, "status": sensor_status[s1]}, \
                                 {"sn": a3, "status": sensor_status[s3]}, \
                                 {"sn": a4, "status": sensor_status[s2]}
    j1, j2, j3, j4 = json.dumps(data1, ensure_ascii=False, sort_keys=False), \
                     json.dumps(data2, ensure_ascii=False, sort_keys=False), \
                     json.dumps(data3, ensure_ascii=False, sort_keys=False), \
                     json.dumps(data4, ensure_ascii=False, sort_keys=False)
    c = j1 + "," + j2 + "," + j3 + "," + j4
    status_data = {"type": "status_msg", "content": c, "uuid": str(uuid.uuid1())}
    out = json.dumps(status_data, ensure_ascii=False, sort_keys=False)
    return out
def main():
    t = check_sensor_status()
    client.on_connect = on_connect
    client.username_pw_set(username, password)
    client.connect("192.168.0.40", 1883, 600)
    client.loop_start()
    d=data_sum()
    client.on_publish = on_publish('device_status_result', d, 2)
    client.loop_stop()

if __name__ == '__main__':
    main()


