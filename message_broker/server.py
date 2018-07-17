import asyncio
import json
import logging
import websockets


logging.basicConfig()

USERS = set()
SUBSCRIPTIONS = {}


async def register(websocket):
    USERS.add(websocket)


async def unregister(websocket):
    USERS.remove(websocket)

    for topic, consumers in SUBSCRIPTIONS.items():
        if websocket in consumers:
            consumers.remove(websocket)


async def notify_consumers(message):
    if message['event_topic'] in SUBSCRIPTIONS:
        # asyncio.wait doesn't accept an empty list
        if SUBSCRIPTIONS[message['event_topic']]:
            await asyncio.wait([consumer.send(json.dumps(message)) for consumer in SUBSCRIPTIONS[message['event_topic']]])


async def forward_messages(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            print(data)
            if data['event_type'] == 'subscription':
                if data['event_topic'] not in SUBSCRIPTIONS:
                    SUBSCRIPTIONS[data['event_topic']] = []

                if websocket not in SUBSCRIPTIONS[data['event_topic']]:
                    SUBSCRIPTIONS[data['event_topic']].append(websocket)

            elif data['event_type'] == 'publication':
                await notify_consumers(data)
            else:
                logging.error("Received unsupported event type: {}", data)
    finally:
        await unregister(websocket)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(forward_messages, 'localhost', 6789))
    asyncio.get_event_loop().run_forever()
