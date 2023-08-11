from kafka import KafkaProducer

TOPIC_NAME = "TWEET"
TWEETS = [
    {
        "message": "Elon Musk is bad for crypto"
    },
    {
        "message": "Elon Musk is a genius"
    },
    {
        "message": "I can't make up my mind about Elon Musk"
    }
]

def publish_message(producer: KafkaProducer, topic_name: str, value: str):
    value_bytes = bytes(value, encoding="utf-8")
    producer.send(topic_name, value=value_bytes)
    producer.flush()
    print("message published!")

if __name__=="__main__":

    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        api_version=(0,11,5),
    )

    for tweet in TWEETS:
        publish_message(
            producer,
            TOPIC_NAME,
            tweet["message"]
        )