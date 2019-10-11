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
            sensor_status[i]=0
t=check_sensor_status()
print(sensor_status)