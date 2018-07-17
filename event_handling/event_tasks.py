# Event generators ...
event_generators = [
    {
        "method": "get_price_file",
        "parameters": {},
        "events_raised": ["PriceDataArrived", "ProcessError"]
    }
]
# Event processors ...
event_processors = [
    {
        "event_topic": "PriceDataArrived",
        "method": "validate_price_file",
        "parameters": {},
        "events_raised": ["PriceDataValidated", "PriceDataInvalidated", "ProcessError"]
    },
    {
        "event_topic": "PriceDataValidated",
        "method": "process_price_file",
        "parameters": {},
        "events_raised": ["PriceDataProcessed", "ProcessError"]
    },
    {
        "event_topic": "PriceDataInvalidated",
        "method": "notify_users",
        "parameters": {"recipients": ["OPERATIONS"]},
        "events_raised": ["ProcessError"]
    },
    {
        "event_topic": "PriceDataProcessed",
        "method": "notify_users",
        "parameters": {"recipients": ["OPERATIONS"]},
        "events_raised": ["ProcessError"]
    },
    {
        "event_topic": "ProcessError",
        "method": "notify_users",
        "parameters": {"recipients": ["ENGINEERING", "OPERATIONS"]},
        "events_raised": ["UserNotification", "ProcessError"]
    }
]
