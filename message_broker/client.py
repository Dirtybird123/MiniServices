import websockets
import json
import uuid


class Client:
    def __init__(self, url):
        self._ws = None
        self._url = url

    async def connect(self):
        self._ws = await websockets.connect(self._url)

    async def disconnect(self):
        await self._ws.close()

    async def register_as_consumer(self, event_topic):
        # register as a consumer ...
        await self._ws.send(json.dumps({"event_type": "subscription",
                                        "event_topic": event_topic}))

    async def receive(self):
        return json.loads(await self._ws.recv())

    async def publish(self, event_topic, event_data, event_trace=[]):
        return await self._ws.send(json.dumps({
            "event_type": "publication",
            "event_id": str(uuid.uuid4()),
            "event_topic": event_topic,
            "event_data": event_data,
            "event_trace": event_trace
        }))
