import json
import paho.mqtt.client as mqtt
import json
from datetime import datetime

mqttBroker = 'add the ip here'
client = mqtt.Client('Iot-Device-Manager')
client.connect(mqttBroker, port=1883, bind_address='')
file = open('iotid.txt', 'r')
deviceId = file.read().splitlines()[0]
file.close()
MQTT_MSG=json.dumps({"deviceName": "RASPBERRY 7", "_id": deviceId, "channels":  ["light", "noise"],  "timestamp": datetime.timestamp(datetime.now()), "disconnect": False});

client.publish('ANNOUNCEMENTS', MQTT_MSG)
