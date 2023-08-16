from kafka import KafkaConsumer

TOPIC_NAME = "tweets"

if __name__=="__main__":

    consumer = KafkaConsumer(
        TOPIC_NAME,
        auto_offset_reset='earliest',
        bootstrap_servers=["localhost:9092"],
        api_version=(0,11,5),
        consumer_timeout_ms=1000,
    )

    for message in consumer:
        print(f"value={message.value}")
