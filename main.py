import asyncio
from event_handling import event_generator, event_processor, event_processor_methods, event_generator_methods, event_tasks

# here we just set up the event loop ...
loop = asyncio.get_event_loop()

all_generator_coroutines = asyncio.gather(*[event_generator.generate_events(
    getattr(event_generator_methods.Methods(), generator['method']),
    generator['parameters']) for generator in event_tasks.event_generators])

all_processor_coroutines = asyncio.gather(*[event_processor.process_events(
    processor['event_topic'],
    getattr(event_processor_methods.Methods(), processor['method']),
    processor['parameters']) for processor in event_tasks.event_processors])

all_coroutines = asyncio.gather(all_generator_coroutines, all_processor_coroutines)

loop.run_until_complete(all_coroutines)
loop.close()



