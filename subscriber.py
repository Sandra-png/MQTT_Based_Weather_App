# The subsciber.py app listens to the MQTT and stores data in a cloud-style database

# This app stores all weather messages in an SQLite Database

# -- IMPORTS --
from paho.mqtt import client as mqtt_client
from mqtt_config import broker_address, broker_port, topic, generate_client_id
import sqlite3
import json
import traceback

# -- STARTUP --
print ("Weather Data Subscriber starting...")
print (f"Connecting to broker at {broker_address}:{broker_port}")
print (f"Subscribing to topic: {topic}")

# -- DATABASE SETUP --
try:
    conn = sqlite3.connect ("/app/weather.db", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute ("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            condition TEXT,
            temperature INTEGER,
            wind_speed INTEGER,
            wind_direction TEXT
        )
    """)
    
    conn.commit()
    print ("SQLite database created.\n")
    
except Exception as db_error:
    print (f"\nDatabase setup failed with error\n: {db_error}")
    traceback.print_exc()

# -- ADDITION TO DATABASE --
def on_message (client, userdata, msg):
    try:
        data = json.loads (msg.payload.decode())
        print ("\nReceived Data:", data)
        
        # Add the data to the database
        cursor.execute ("""
            INSERT INTO weather 
                (timestamp, 
                condition, 
                temperature, 
                wind_speed, 
                wind_direction)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data.get ("timestamp"),
            data.get ("condition"),
            data.get ("temperature"),
            data.get ("wind_speed"),
            data.get ("wind_direction")
        ))
        
        conn.commit()
        
        print ("\nData saved to database.\n")
    
    except Exception as e:
        print ("\nError occured: \n", e)
        traceback.print_exc()


# -- SUBSCRIPTION TO TOPIC --
def on_connect (client, userdata, flags, rc, properties = None):
    if rc == 0:
        print ("Subscriber connected to MQTT broker.\n")
        client.subscribe (topic)
        print (f"Subscribed to topic: {topic}")
    else:
        print (f"Failed to connect, return code {rc}\n")


# -- MQTT CLIENT SETUP --
client_id = generate_client_id ("subscriber")
client = mqtt_client.Client (mqtt_client.CallbackAPIVersion.VERSION2, client_id)
client.on_connect = on_connect
client.on_message = on_message

print (f"MQTT Client ID: {client_id}\n")


# -- CONNECT AND RUN --
try:
    client.connect (broker_address, broker_port)
    client.loop_forever()
    
except Exception as e:
    print ("\nError occured: \n", e)
    traceback.print_exc()

finally:
    conn.close()
    print ("\nSQLite database connection closed.")