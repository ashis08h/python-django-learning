# observer interface


class Subscriber:

    def update(self, news):
        pass


class EmailSubscriber(Subscriber):

    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received News: {news}")


# subject

class NewsAgency:

    def __init__(self):
        self.subscribers = []
        self.news = None

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_all(self):
        for subscriber in self.subscribers:
            subscriber.update(self.news)

    def add_news(self, news):
        print(f"\nNews Agency posted: {news}")


agency = NewsAgency()
s1 = EmailSubscriber("Ashish")
s2 = EmailSubscriber("Kumar")

agency.add_subscriber(s1)
agency.add_subscriber(s2)

agency.add_news("New python 4.0 released!")
agency.add_news("Django 5.0 is not live.")