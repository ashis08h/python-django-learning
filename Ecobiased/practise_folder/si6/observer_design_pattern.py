class Subject:

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify_observer(self, value):
        for observer in self._observers:
            observer.update(value)


class Observer:
    def update(self, value):
        pass


class ConcreteObserver(Observer):
    def update(self, value):
        print(f"Received update with value {value}")


subject = Subject()

observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.notify_observer("Hello Observers!")

subject.detach(observer2)
subject.notify_observer('Second again!')