import asyncio
import json


# classes to contain static methods for
# the actual event generating business logic
class Methods:
    @staticmethod
    async def get_price_file(parameters):
        await asyncio.sleep(5)
        return [('PriceDataArrived', json.dumps({"AAPL.OQ": 234.12, "MSFT.OQ": 234.12}))]

