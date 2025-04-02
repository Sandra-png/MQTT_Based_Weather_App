# 🌤️ Weather MQTT Client (Python + Docker)

**Author:** Sandra  
**Project Type:** IoT Data Publisher  
**Tags:** MQTT, Python, Docker, EMQX, Paho

## Description

This project simulates a weather sensor using Python and publishes mock weather data to an MQTT broker every 60 seconds. It's built with the `paho-mqtt` client library and runs inside a Docker container for easy portability.

---

# Features
- Publishes random weather data every 60 seconds
- Uses a public MQTT broker (`broker.emqx.io`)
- Works standalone with Python or in a Docker container

---

## How to Replicate

### Clone the Repo

```bash
git clone https://github.com/Sandra-png/MQTT-based-Weather-App/tree/main
```

### Option 1: Run with Docker
Run these commands in the terminal to build the client, and then run it:
```bash  
  docker build -t weather-client .
  docker run --rm weather-client
```

### Option 2: Run Locally with Python
Install dependencies
```bash
  pip install paho-mqtt
```

Run the script in the terminal
```bash
  python weather_client.py
```


## Example Output in Terminal
```bash
Weather MQTT Client starting...
MQTT Broker Configured at: broker.emqx.io:1883

MQTT Client Initialized.

Connected to MQTT broker.

Publishing Weather:
{'Time: ': 1711473251, 'Weather Conditions: ': 'Clouded', 'Temperature: ': 22, 'Wind Speed: ': 7, 'Wind Direction: ': 'West'}

Message sent to topic 'python/mqtt'
```

## Output on the Flask-Web Application
<img width="651" alt="bilde" src="https://github.com/user-attachments/assets/eeda37f8-fb50-444e-b754-78bcb198d8fa" />

