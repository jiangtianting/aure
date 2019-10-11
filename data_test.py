import json
import uuid
a1,a2,a3,a4="server_wendu","server_atp","server_light","server_co2"
s1,s2,s3,s4="BMP180_1.py","co2_1.py","gy_30.py","gpio.py"
sensor_status={s1:1,s2:1,s3:1,s4:1}
data1,data2,data3,data4= {"sn": a1, "status":sensor_status[s4]},\
             {"sn": a2, "status": sensor_status[s1]},\
             {"sn": a3, "status": sensor_status[s3]},\
             {"sn": a3, "status": sensor_status[s2]}
print(data1,data2,data3,data4)
j1,j2,j3,j4 = json.dumps(data1, ensure_ascii=False, sort_keys=False),\
     json.dumps(data2, ensure_ascii=False, sort_keys=False),\
     json.dumps(data3, ensure_ascii=False, sort_keys=False),\
     json.dumps(data4, ensure_ascii=False, sort_keys=False)
c = j1 + "," + j2 + "," + j3 + "," + j4
status_data = {"type": "status_msg", "content": c, "uuid": str(uuid.uuid1())}
out = json.dumps(status_data, ensure_ascii=False, sort_keys=False)
print(c)