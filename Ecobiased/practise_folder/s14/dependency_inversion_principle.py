class EmailService:

    def send(self, message):
        print(f"Sending email {message}")


class NotificationManager:

    def __init__(self):
        self.email_service = EmailService() # TIGHLY COUPLED.

    def send_alert(self):
        self.email_service.send("Alert Triggered")

# Notification manager is tightly coupled with EmailService.
# What if tomorrow you want to switch to SMSService? You will need to edit this class.
# Violates open/close principle too.


class Notifier:

    def send(self, message):
        raise NotImplementedError


class EmailService1(Notifier):

    def send(self, message):
        print(f"Sending Email: {message}")


class SMSService1(Notifier):

    def send(self, message):
        print(f"Sending SMS: {message}")


class NotificationManager1:

    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send_alert(self):
        self.notifier.send("Alert Triggered.")


email = EmailService1()
sms = SMSService1()

manager = NotificationManager1(email)
manager.send_alert()

manager = NotificationManager1(sms)
manager.send_alert()

