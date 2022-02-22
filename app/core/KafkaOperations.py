from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer
from kafka import KafkaConsumer
from app import Config


def get_consumer_groups(user):
    consumer = KafkaAdminClient(group_id=user.user_id, bootstrap_servers=Config.Links.KAFKA_HOSTS)
    for group in consumer.list_consumer_groups():
        print(group[0])


def create_room_topic(room_name):
    admin_client = KafkaAdminClient(bootstrap_servers=Config.Links.KAFKA_HOSTS)
    topic_list = []
    topic_list.append(NewTopic(name=room_name, num_partitions=1, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)


def send_message_in_room(room_name):
    producer = KafkaProducer(bootstrap_servers=Config.Links.KAFKA_HOSTS)
    message_data = input("Enter message: ")
    producer.send(room_name, str.encode(message_data))
    print("Message Sent!")


def read_messages_in_room(room_name):
    consumer = KafkaConsumer(room_name, bootstrap_servers=Config.Links.KAFKA_HOSTS, auto_offset_reset='earliest')
    consumer.subscribe(room_name)
    for msg in consumer:
        print(f"Message from Producer on room - {msg.topic}: \"{msg.value.decode()}\"")

