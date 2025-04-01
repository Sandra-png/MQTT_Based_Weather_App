FROM python:3.10.12

RUN pip install --no-cache-dir paho-mqtt 

COPY weather_client.py /app/


CMD ["python", "-u", "/app/weather_client.py"]