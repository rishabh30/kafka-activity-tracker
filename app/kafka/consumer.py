import logging
from aiokafka import AIOKafkaConsumer

from app.kafka.event_handler import event_handler
from app.kafka.configs import KafkaConfig
from app.kafka.constants import ConsumerConstants


class KafkaMessageConsumer:
    """
    KafkaMessageConsumer is a singleton class that handles reading messages from Kafka.

    It uses AIOKafkaConsumer to read messages from the topics listed in
    ConsumerConstants.topics_to_consume, ensuring that only one instance is used in the entire application.

    Attributes:
        _instance (KafkaMessageConsumer): The singleton instance of the class.
        _consumer (AIOKafkaConsumer): The Kafka consumer instance.

    Methods:
        start(): Asynchronously starts the Kafka consumer.
        consume(): Asynchronously consumes messages from the Kafka topics and processes them.
        stop(): Asynchronously stops the Kafka consumer.
    """

    _instance = None
    _consumer = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._consumer = AIOKafkaConsumer(
                *ConsumerConstants.topics_to_consume,
                bootstrap_servers=KafkaConfig.BOOTSTRAP_SERVER,
                group_id=KafkaConfig.GROUP_NAME,
                auto_offset_reset=KafkaConfig.AUTO_OFFSET_RESET,
            )
        return cls._instance

    async def start(self):
        if self._consumer is not None:
            await self._consumer.start()

    async def consume(self):
        if self._consumer is not None:
            try:
                async for message in self._consumer:
                    logging.info(
                        f"Consumed topic: {message.topic}, value: {message.value}"
                    )
                    await event_handler(message.topic, message.value)
            except Exception as e:
                logging.error(f"Error consuming messages: {e}")

    async def stop(self):
        if self._consumer is not None:
            await self._consumer.stop()
