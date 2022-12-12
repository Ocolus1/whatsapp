from twilio.rest import Client
from django.conf import settings


def get_client():
    account_sid, auth_token = settings.ACCOUNT_SID, settings.AUTH_TOKEN
    client = Client(account_sid, auth_token)
    return client
