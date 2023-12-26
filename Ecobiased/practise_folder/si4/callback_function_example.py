class EventSystem:

    def __init__(self):
        self.events = {}

    def register_events(self, event_name, callback):
        if event_name in self.events:
            self.events[event_name].append(callback)
        else:
            self.events[event_name] = [callback]

    def trigger_events(self, event_name, data):
        if event_name in self.events:
            for callback in self.events[event_name]:
                callback(data)


def button_click(data):
    print(f"Button click with data {data}.")


def on_mouse_move(data):
    print(f"Mouse move to coordinates: {data}")


event_sys = EventSystem()
event_sys.register_events("button_click", button_click)
event_sys.register_events("button_click", button_click)
event_sys.register_events("mouse_move", on_mouse_move)

event_sys.trigger_events("button_click", "submit")
event_sys.trigger_events("mouse_move", (100, 200))

