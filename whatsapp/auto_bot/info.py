from twilio.rest import Client



def get_client():
    account_sid, auth_token = "ACb0781ddff8f84951d091eafe3a09b372", "a5eab65c6e86416e76cab773c62f994d"
    client = Client(account_sid, auth_token)
    return client
