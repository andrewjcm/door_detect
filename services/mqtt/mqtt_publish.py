from paho.mqtt.client import Client, MQTTv5
from config import settings
from services.mqtt.schema import MqttPayload


class MqttPublish:
    username: str = settings.MQTT_USERNAME
    password: str = settings.MQTT_PASSWORD
    host: str = settings.MQTT_HOST
    topic: str = settings.MQTT_TOPIC
    client: Client
    message: MqttPayload

    def __init__(self, message: dict) -> None:
        self.client = Client(
            transport="tcp",
            protocol=MQTTv5
        )
        self.client.username_pw_set(username=self.username, password=self.password)
        self.client.connect(host=self.host)
        self.message = MqttPayload(**message)

    def send(self):
        self.client.publish(topic=self.topic, payload=self.message.model_dump_json(), retain=True)

    def close(self):
        self.client.disconnect()
