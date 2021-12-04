from __future__ import print_function
from os import error
import paho.mqtt.publish as publish
# from bmp180 import bmp180
from time import sleep
# import smbus
import sys
import time
channelID = "1596331"  #Enter your Channel ID here
apiKey = "8V5G5U40PHOR7FOK"  #Enter your WriteAPI key here
useUnsecuredTCP = True
useUnsecuredWebsockets = False
useSSLWebsockets = False


mqttHost = "mqtt.thingspeak.com"


if useUnsecuredTCP:
    tTransport = "tcp"
    tPort = 1883
    tTLS = None

if useUnsecuredWebsockets:
    tTransport = "websockets"
    tPort = 80
    tTLS = None

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    tPort = 443
        
topic = "channels/" + channelID + "/publish/" + apiKey

f=open("data.txt")
sensor =f.read()
temp = ""
voltage= ""
LDR1=""
LDR2=""
LDR3=""
LDR4=""
SM1=""
SM2=""

for i in sensor.split('\n'):
# while(True):
    k=i.split(', ')
    print(k)
    temp = k[1]
    voltage= k[0]
    LDR1=k[2] #top left
    LDR2=k[3] #top right
    LDR3=k[4] #bottom left
    LDR4=k[5] #bottom right
    SM1=k[6] #servo up down
    SM2=k[7]#servo right left
    
        # print ("Temperature =",temp ,"Voltage =", voltage,"LDR1=", LDR1,"LDR2 =", LDR2,"LDR3 =", LDR3,"LDR4 =", LDR4,"SM1=", SM1,"SM2 =", SM2)

    tPayload = "field1=" + str(temp) + "&field2=" + str(voltage) + "&field3=" +str(LDR1) + "&field4=" +str(LDR2) + "&field5=" +str(LDR3)+ "&field6=" +str(LDR4)+ "&field7=" +str(SM1)+ "&field8=" +str(SM2)    
    
    try:
        publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
        time.sleep(5)

    except (KeyboardInterrupt):
        break

    except Exception as E:
        print (E)
