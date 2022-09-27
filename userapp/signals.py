from django.dispatch import Signal,receiver
notification = Signal(providing_args=["requests","users"])

@receiver(notification)
def send_emails(sender,**kwargs):
    print(sender)
    