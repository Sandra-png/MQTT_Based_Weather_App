# This project demonstrates MQTT communication using Python.
# The weather_client.py generates randomized weather data every 60 seconds, and publishes it to a public MQTT broker

# -- IMPORTS --
from paho.mqtt import client as mqtt_client
from mqtt_config import broker_address, broker_port, topic, publish_interval, generate_client_id
import json
import random
import time
import traceback

print ("Weather MQTT Client starting...")
print (f"MQTT Broker Configured at: {broker_address}:{broker_port}\n")

# -- CLIENT SETUP --
def on_connect (client, userdata, flags, rc, properties = None):
    if rc == 0:
        print ("Connected to MQTT broker.\n")
    else:
        print (f"Failed to connect, return code {rc}\n")

client = mqtt_client.Client (mqtt_client.CallbackAPIVersion.VERSION2, generate_client_id ("weather-client"))
client.on_connect = on_connect

print ("MQTT Client Initialized. \n")

# -- MAIN LOOP --
try:
    # Connecting to the MQTT broker
    client.connect (broker_address, broker_port)
    client.loop_start() # Starting the network loop in the background

    # Slight delay so subscriber can connect before the first message gets sent
    time.sleep (5)

    # Continuous loop to publish data according to the publish interval
    while True:
        print ("Generating mock weather data...\n")
        
        # When called upon, the weather data will be randomly generated:
        weather_condition = random.choice (["Sunny", "Raining", "Snowing", "Clouded"])
        temperature = random.randint (-10, 30)
        wind_speed = random.randint (0, 21)
        wind_direction = random.choice (["North", "East", "West", "South"])

        weather_data = {
            "timestamp": int(time.time()),
            "condition": weather_condition,
            "temperature": temperature,
            "wind_speed": wind_speed,
            "wind_direction": wind_direction,
        }
        
        print ("Publishing Weather:\n", weather_data)


        # Turning weather_data to a JSON string, to publish it to the client
        result = client.publish (topic, json.dumps(weather_data))
        status = result [0]

        if status == 0:
            print (f"\nMessage sent to topic '{topic}'")
        else:
            print (f"\nFailed to send message to topic '{topic}'")

        # Wait-time before next publication
        time.sleep (publish_interval)

except Exception as e:
    print ("Error:", e)
    traceback.print_exc()

finally:
    client.loop_stop()
    client.disconnect()
    print ("\nMQTT Client has successfully disconnected.\n")