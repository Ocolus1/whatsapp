import logging

from celery import shared_task

from whatsapp.users.models import User

from .info import get_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@shared_task(name="computation_heavy_task")
def computation_heavy_task(setup_id):
    setup_id = setup_id.lower()
    client = get_client()
    user = User.objects.get(name=setup_id)
    message = client.messages \
    .create(
        body= \
            f"""Hello {user.name}!
            \nSend the list of things you have done today.
            \nIn this format---
            \nJohn
            \n1. I woke up
            \n2. I ate
            \n3. I slept
            """,
        from_='whatsapp:+14155238886',
        to=f'whatsapp:+{user.phone}'
     )

    print(message.sid, flush=True)


@shared_task(name="send_to_group")
def send_to_group():
    client = get_client()
    users = User.objects.all()
    response = []
    phones = []
    updated_At = []
    for user in users:
        response.append(user.activity)
        phones.append(user.phone)
        updated_At.append(user.updated_at)

    message = client.messages \
    .create(
        body= \
            f"""
            Everyone activities for the day!
            \n{response[1]} {updated_At[1]}
            \n{response[2]} {updated_At[2]}
            \n{response[3]} {updated_At[3]}
            """,
        from_='whatsapp:+14155238886',
        to=f'whatsapp:+{phones[3]}'
     )

    print(message.sid, flush=True)

