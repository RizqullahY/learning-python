import paho.mqtt.client as mqtt
# from paho.mqtt import client as mqtt_client

# define static variable
# broker = "localhost" # for local connection
broker = "test.mosquitto.org"  # for online version
port = 1883
timeout = 60

username = ''
password = ''

topic = "aquathings/lampu"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic,qos=2)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    payload_decoded = msg.payload.decode('utf-8')
    if payload_decoded == "On":
        print("Lampu dinyalakan")
        # Do something
        
    elif payload_decoded == "Off":
        print("Lampu dimatikan")
        # Do something else
    else:
        print("perintah tidak di kenali")
          
        
# Create an MQTT client and attach our routines to it.
client = mqtt.Client("device0")
client.username_pw_set(username=username,password=password)
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(broker, port, timeout)

client.loop_forever()
