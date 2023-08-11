from kafka import KafkaConsumer

TOPIC_NAME = "TWEET"

if __name__=="__main__":

    consumer = KafkaConsumer(
        TOPIC_NAME,
        auto_offset_reset='earliest',
        bootstrap_servers=["localhost:9092"],
        api_version=(0,11,5),
        consumer_timeout_ms=1000,
    )

    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
    