from paho.mqtt import client as mqtt_client
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import json

broker = "test.mosquitto.org"
port = 1883
topic = "pucv/iot/m6/p3/g2000"

token ="token"
org = "org"
url = "url"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket = "bucket"

write_api = client.write_api(write_options=SYNCHRONOUS)


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client):
    def on_message(client, userdata, msg):
        data = json.loads(msg.payload)

        point1 = (
            Point("sensores")
            .tag("device_id", data['device_id'])
            .field("temperature", data['temperature'])
            .field("humedad", data['humidity'])
                )
        write_api.write(bucket=bucket, org=org, record=point1)


        print(f"Received from Device: { data }")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever() #publica para siempre

if __name__ == '__main__':
    run()