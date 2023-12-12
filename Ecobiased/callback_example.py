class EventSystem:
    def __init__(self):
        self.events = {}

    def register_event(self, event_name, callback):
        if event_name in self.events:
            self.events[event_name].append(callback)
        else:
            self.events[event_name] = [callback]

    def trigger_event(self, event_name, data=None):
        if event_name in self.events:
            for callback in self.events[event_name]:
                callback(data)


# Create an instance of the EventSystem
event_system = EventSystem()


# Define callback functions
def on_button_click(data):
    print(f"Button clicked with data: {data}")


def on_mouse_move(data):
    print(f"Mouse moved to coordinates: {data}")


# Register event handlers
event_system.register_event("button_click", on_button_click)
event_system.register_event("mouse_move", on_mouse_move)

# Simulate button click and mouse move events
event_system.trigger_event("button_click", "Submit")
event_system.trigger_event("mouse_move", (100, 200))