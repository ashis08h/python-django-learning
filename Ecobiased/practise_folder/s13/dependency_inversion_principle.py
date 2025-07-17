class EmailService:

    def send(self, message):
        print(f"sending email: {message}")


class NotificationManager:

    def __init__(self):
        self.email_service = EmailService() # tightly coupled

    def send_alert(self):
        self.email_service.send("Alert triggered")

#  NotificationManager is tightly coupled to EmailService
# What if tomorrow you want to switch to SMSService? you will need to edit this class
# Violates Open/Close principle too.


class Notifier:

    def send(self, message):
        raise NotImplementedError


class EmailService1(Notifier):
    def send(self, message):
        print(f"sending Email: {message}")


class SMSService1(Notifier):
    def send(self, message):
        print("sending SMS")


class NotificationManager1:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send_alert(self):
        self.notifier.send("Alert trigger")


email = EmailService1()
sms = SMSService1()

manager = NotificationManager1(email)
manager.send_alert()

manager = NotificationManager1(sms)
manager.send_alert()