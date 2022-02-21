from kafka import KafkaConsumer
from kafka import KafkaProducer

KAFKA_HOSTS = ['localhost:9092']
topic = 'foobars'

producer = KafkaProducer(bootstrap_servers=KAFKA_HOSTS)
print("Sending messages...")
for i in range(1, 20):
    print(i)
    producer.send(topic, b'some_message_bytes')
producer.flush()

print("Receiving messages...")
consumer = KafkaConsumer(topic,
                         bootstrap_servers=KAFKA_HOSTS,
                         group_id=None,
                         enable_auto_commit=False,
                         auto_offset_reset='smallest')
for msg in consumer:
    print(msg)

producer.close()
