import network
from umqtt.simple import MQTTClient
from machine import Pin
import machine
import ubinascii

 

led = Pin(16, Pin.OUT)
msg1= " "
CONFIG = {

     # Configuration details of the MQTT broker

     "MQTT_BROKER": "test.mosquitto.org",

     "USER": "",

     "PASSWORD": "",

     "PORT": 1883,

     "TOPIC": b"test",

     # unique identifier of the chip

     "CLIENT_ID": b"esp8266_" + ubinascii.hexlify(machine.unique_id())

}
   

       

def settimeout(duration):

    pass

 

station=network.WLAN(network.STA_IF)

station.active(True)

station.connect("sandeep", "22122012")

while (not (station.isconnected())):

        print("waiting to Connect")

        print (station.ifconfig())

        time.sleep(1)

station.ifconfig()

print ("Connected")

 

print("Connected to Wifi\n")

client = MQTTClient("demo", "broker.hivemq.com", port=1883)

client.settimeout = settimeout

client.connect()

 

 

 

def listen():

    #Create an instance of MQTTClient

    client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], port=CONFIG['PORT'])

    # Attach call back handler to be called on receiving messages

    client.set_callback(onMessage)

    client.connect()

    client.publish("test1", "ESP8266 is Connected")

    client.subscribe(CONFIG['TOPIC'])

    print("ESP8266 is Connected to %s and subscribed to %s topic" % (CONFIG['MQTT_BROKER'], CONFIG['TOPIC']))

 

    try:

        while True:

            msg = client.wait_msg()

           

            #msg = client.check_msg()

            if msg1=="on":

              client.publish("stat","LED ON")

            if msg1=="off":

              client.publish("stat","LED OFF")

    finally:

        client.disconnect() 

 

 

def onMessage(topic, msg):

    print("Topic: %s, Message: %s" % (topic, msg))

    global msg1

    if msg == b"on":

       

        led.value(0)

        msg1="on"

       

       

    elif msg == b"off":

        msg1="off"

        led.value(1)

 

 

listen()