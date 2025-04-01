# Author: Sandra
# Description: An IoT client that simulates weather sensor data and publishes it to an MQTT broker
# This project demonstrates MQTT communication using Python.


# All imports
from paho.mqtt import client as mqtt_client
import json
import random
import time
import traceback

print ("Weather MQTT Client starting...")

# -- CONFIGURATION --
broker_address = "broker.emqx.io" # Public test broker

# This is the default port for MQTT over plain TCP, with no encryption
broker_port = 1883

# Other variables
topic = "python/mqtt"
publish_interval = 60 # in seconds

print (f"MQTT Broker Configured at: {broker_address}:{broker_port}\n")


# -- CLIENT SETUP --
def on_connect (client, userdata, flags, rc, properties = None):
    if rc == 0:
        print ("Connected to MQTT broker.\n")
    else:
        print (f"Failed to connect, return code {rc}\n")

# Generate a unique client ID
client_id = f"weather-client-{random.randint (0, 1000)}"

# Generating a unique client ID
client = mqtt_client.Client (mqtt_client.CallbackAPIVersion.VERSION2, client_id)
client.on_connect = on_connect

print ("MQTT Client Initialized. \n")

try:
    # Connecting to the MQTT broker
    client.connect (broker_address, 1883)
    client.loop_start() # Starting the network loop in the background

    # Continuous loop to publish data according to the publish interval
    while True:
        print ("Generating mock weather data...\n")
        
        # When called upon, the weather data will be randomly generated:
        weather_condition = random.choice (["Sunny", "Raining", "Snowing", "Clouded"])
        temperature = random.randint (-10, 30)
        wind_speed = random.randint (0, 21)
        wind_direction = random.choice (["North", "East", "West", "South"])

        weather_data = {
            "Time: ": int (time.time()),
            "Weather Conditions: ": weather_condition,
            "Temperature: ": temperature,
            "Wind Speed: ": wind_speed,
            "Wind Direction: ": wind_direction,
        }
        
        print ("Publishing Weather:\n", weather_data)


        # Turning weather_data to a JSON string
        result = client.publish (topic, json.dumps(weather_data))
        status = result [0]

        if status == 0:
            print (f"\nMessage sent to topic '{topic}'")
        else:
            print (f"\nFailed to send message to topic '{topic}'")

        # Wait-time before next publication, mostly for testing purposes
        time.sleep (publish_interval)

except Exception as e:
    print ("Error:", e)
    traceback.print_exc()

finally:
    client.loop_stop()
    client.disconnect()
    print ("\nMQTT Client has successfully disconnected.\n")