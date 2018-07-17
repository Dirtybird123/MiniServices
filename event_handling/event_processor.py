from message_broker.client import Client


async def process_events(event_topic, event_handler, event_handler_parameter):
    message_broker_client = Client('ws://localhost:6789')
    await message_broker_client.connect()
    await message_broker_client.register_as_consumer(event_topic)
    try:
        while True:
            message = await message_broker_client.receive()
            event_trace = message['event_trace']+[message['event_id']]
            events_to_publish = await event_handler(
                message['event_data'], event_handler_parameter)
            for publication_topic, publication_data in events_to_publish:
                await message_broker_client.publish(
                    publication_topic, publication_data, event_trace)
    finally:
        await message_broker_client.disconnect()

