from django.conf import settings

import twilio
from twilio.rest import Client

def send_twilio_message(to_number, body):

    account_sid=settings.TWILIO_ACCOUNT_SID
    token=settings.TWILIO_AUTH_TOKEN
    client=Client(account_sid, token)
    # client = twilio.rest.TwilioRestClient(
        # settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    return client.messages.create(
        body=body,
        to=to_number,
        from_=settings.TWILIO_DEFAULT_CALLERID
    )
    