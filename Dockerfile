FROM python:3.10.12
WORKDIR /app

RUN pip install --no-cache-dir paho-mqtt 

COPY flask_app.py mqtt_config.py /app/


CMD ["python", "-u", "/app/weather_client.py"]