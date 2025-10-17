class EmailService:

    def send(self, message):
        print(f"Sending email {message}")


class NotificationManager:

    def __init__(self):
        self.email_service = EmailService() # Tightly coupled.

    def send_alert(self):
        self.email_service.send("Alert Trigger")


# In the above example NotificatioManager is tightly coupled with EmailService
# What if tomorrow if we wanted to switch to SMS service, then you will need to edit the class.
# violates open/close principle too.

class Notifier:

    def send(self, message):
        raise NotImplementedError


class EmailService1(Notifier):

    def send(self, message):
        print(f"Sending email with message {message}")


class SMSService1(Notifier):

    def send(self, message):
        print(f"Sending SMS with message {message}")


class NotificationManager1:

    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send_alert(self):
        self.notifier.send("Alert Trigger")


email = EmailService1()
sms = SMSService1()

manager = NotificationManager1(email)
manager.send_alert()

manager = NotificationManager1(sms)
manager.send_alert()