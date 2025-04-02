# I use the config in two different files, so I created one file to keep it in for better organization.
# Includes:
# -  Broker Address
# -  Broker Port
# -  Topic
# -  Publication Interval
# -  Client ID generation

# -- IMPORTS --
import uuid

# -- CONFIGURATION --
broker_address = "broker.emqx.io" # Public test broker
broker_port = 1883 # Default port for MQTT over plain TCP
topic = "python/mqtt"
publish_interval = 60 # in seconds

def generate_client_id (prefix = "client"):
    # Client id is generated using UUID (Universally Unique Identifiers)
    return f"{prefix}-{uuid.uuid4()}"