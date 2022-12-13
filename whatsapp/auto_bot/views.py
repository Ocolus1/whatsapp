from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse
from .info import get_client
from whatsapp.users.models import User

@csrf_exempt
def twilio(request):

    # # user input
    # user_msg = request.POST.get('Body').lower()

    # # creating object of MessagingResponse
    # response = MessagingResponse()

    # # User Query
    # name = user_msg.split()[0].lower()
    # if User.object.filter(name=name).exists():
    #     user = User.object.get(name=name)
    #     user.activity = user_msg
    #     user.save()

    # # list to store urls
    # response.message("Your response has been saved")
    user_msg = request.values.get('Body', '').lower()
    print("hope this works", flush=True)
    print(request.values, flush=True)

    # creating object of MessagingResponse
    response = MessagingResponse()

    # User Query
    q = user_msg + "geeksforgeeks.org"

    # list to store urls
    result = []

    # searching and storing urls
    # for i in search(q, tld='co.in', num=6, stop=6, pause=2):
    #     result.append(i)

    # displaying result
    msg = response.message(f"--- Result for '{user_msg}' are  ---")

    # msg = response.message(result[0])
    # msg = response.message(result[1])
    # msg = response.message(result[2])
    # msg = response.message(result[3])
    # msg = response.message(result[4])

    return HttpResponse(str(response))
