from twilio.rest import Client

TWILIO_SID = "SID"
TWILIO_AUTH_TOKEN = "AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER = "VIR_NUMB"
TWILIO_VERIFIED_NUMBER = "VER_NUMB"

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)
        