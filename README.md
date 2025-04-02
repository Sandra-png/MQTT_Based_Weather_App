# 🌤️ Weather MQTT Client (Python + Docker + Flask)

**Author:** Sandra  
**Project Type:** IoT Data Publisher & Web Dashboard
**Tags:** MQTT, Python, Docker, Flask, EMQX, Paho, SQLite

## Description
This project simulates a weather sensor using Python and publishes mock weather data to an MQTT broker every 60 seconds. A subscriber listens to these messages and stores the weather data in ann SQLite database. A Flask-based web dashboard displays previous and new weather information. Each component runs inside its own docker container.

---

# Features
- Publishes random weather data every 60 seconds
- Uses a public MQTT broker (`broker.emqx.io`)
- A subscriber receives MQTT messages and stores them in an SQLite database
- A Flask application displays the stored weather data
- Each component runs in a Docker container with easy setup, via a Docker Compose

---

# Project Structure
```
├── README.md
├── docker-compose.yml
├── data/                   # Persistent SQLite database storage
├── mqtt_config/
│   ├── __init__.py
│   └── mqtt_config.py      # Shared MQTT configuration
├── subscriber/
│   ├── Dockerfile.subscriber
│   └── subscriber.py       # Listens and stores weather data
├── weather_client/
│   ├── Dockerfile.weather
│   └── weather_client.py   # Publishes weather data
└── web_dashboard/
    ├── Dockerfile.flask
    └── flask_app.py        # Displays weather data via web
```

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/Sandra-png/MQTT-based-Weather-App/tree/main
```

### Run with Docker
Run these commands in the terminal to build the client, and then run it:
```bash  
  docker build -t weather-client .
  docker run --rm weather-client
```

### Open the Flask Web Dashboard
```
http://localhost:5050
```

## Example Output in Terminal
```bash
weather-client-1  | 2025-04-02T14:16:54.722843126Z Generating mock weather data...
2025-04-02 16:16:54 weather-client-1  | 
2025-04-02 16:16:54 weather-client-1  | Publishing Weather:
2025-04-02 16:16:54 weather-client-1  |  {'timestamp': 1743603414, 'condition': 'Sunny', 'temperature': 21, 'wind_speed': 19, 'wind_direction': 'East'}
2025-04-02 16:16:54 weather-client-1  | 
2025-04-02 16:16:54 weather-client-1  | Message sent to topic 'python/mqtt'
2025-04-02 16:16:54 subscriber-1      | 
2025-04-02 16:16:54 subscriber-1      | Received Data: {'timestamp': 1743603414, 'condition': 'Sunny', 'temperature': 21, 'wind_speed': 19, 'wind_direction': 'East'}
2025-04-02 16:16:54 subscriber-1      | 
2025-04-02 16:16:54 subscriber-1      | Data saved to database.
2025-04-02 16:16:54 subscriber-1      | 
```

## Output on the Flask-Web Application
<img width="651" alt="bilde" src="https://github.com/user-attachments/assets/eeda37f8-fb50-444e-b754-78bcb198d8fa" />

