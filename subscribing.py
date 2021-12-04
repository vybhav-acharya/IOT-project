import paho.mqtt.client as mqtt
import json

apiKey = "8V5G5U40PHOR7FOK"

channelID = "1596331"
apiKey = "GIY4IWN9CX9SVY52"

# This is the Subscriber
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("channels/" + channelID + "/subscribe/fields/+")


def on_message(client, userdata, msg):
    print("ubbus")
    print(json.loads(msg.payload)) #converting the string back to a JSON object

client = mqtt.Client()
# if (!client.isConnected()) {
#             client.connect( " PhotonSubscribeXX" , "Username" , MQTTAPIKey , NULL , MQTT::QOS0 , 0 , NULL , true );
#             Particle.publish( " Connect " );
#             delay( 1000 );
#             if ( client.isConnected())   {
      
#                 //client.subscribe("channels/739/subscribe/fields/field2");
#                 client.subscribe( subscribeTopic );
#                 Particle.publish( "subs" );
#                 }
#      }
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.thingspeak.com", 1883, 60)

client.loop_forever()