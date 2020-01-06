import os

tel = os.environ.get('TWILIO_TELEPHONE_NUMBER')
account_token = os.environ.get('TWILIO_AUTH_TOKEN')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twil = os.environ.get('TWILIO_DEFAULT_CALLERID')