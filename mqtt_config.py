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

# This is the default port for MQTT over plain TCP, with no encryption
broker_port = 1883

# Other variables
topic = "python/mqtt"
publish_interval = 60 # in seconds

def generate_client_id (prefix = "client"):
    # Client id is generated using UUID (Universally Unique Identifiers)
    return f"{prefix}-{uuid.uuid4()}"