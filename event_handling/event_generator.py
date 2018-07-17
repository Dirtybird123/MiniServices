from message_broker.client import Client


async def generate_events(event_generator_method, event_generator_parameter):
    message_broker_client = Client('ws://localhost:6789')
    await message_broker_client.connect()
    try:
        while True:
            events_to_publish = await event_generator_method(event_generator_parameter)
            for publication_topic, publication_data in events_to_publish:
                await message_broker_client.publish(publication_topic, publication_data)
    finally:
        await message_broker_client.disconnect()
