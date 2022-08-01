
class EventHandler:
    def __init__(self, event_stirage: AbstractEventStorage):
        self.event_storage = event_stirage

    async def handle(self, event):
        event_await self.event_storage.send_event(event)




def get_event_handler(
        event_storage: AbstractEventStorage = Depends(get_kafka)
)->EventHandler:

    return EventHandler(event_storage)