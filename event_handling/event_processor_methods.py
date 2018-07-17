import json


# Classes to contain static methods for
# the actual event processing business logic.
class Methods:
    @staticmethod
    async def validate_price_file(data, parameters):
        """Validates a price file and raises a 'PriceDataValidated' and or 'PriceDataInvalidated' event."""
        data_parsed = json.loads(data)
        return [
            ('PriceDataValidated', json.dumps(data_parsed["AAPL.OQ"])),
            ('PriceDataInvalidated', (json.dumps({"MSFT.OQ": data_parsed["MSFT.OQ"]}), "Unknown RIC.")),
        ]

    @staticmethod
    async def process_price_file(data, parameters):
        """Processes a price file and raises a 'PriceDataProcessed' event."""
        return [('PriceDataProcessed', data)]

    @staticmethod
    async def notify_users_success(data, parameters):
        """Notifies users about an event raised."""
        data_parsed = json.loads(data)
        for recip in parameters['recipients']:
            pass
        return [('UserNotificationSuccess', (data, "Notified user(s) %s of event '%s.'" % (parameters['recipients'], data_parsed['event_trace'][-1])))]

    @staticmethod
    async def notify_users_error(data, parameters):
        """Notifies users about an event raised."""
        for recip in parameters['recipients']:
            pass
        return [('UserNotificationError', data)]
