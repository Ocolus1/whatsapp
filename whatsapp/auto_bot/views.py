from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse
from .info import get_client
from whatsapp.users.models import User

@csrf_exempt
def twilio(request):

    # user input
    user_msg = request.POST.get('Body').lower()

    # creating object of MessagingResponse
    response = MessagingResponse()

    # User Query
    q = user_msg
    name = user_msg.split()[0].lower()
    if User.object.filter(name=name).exists():
        user = User.object.get(name=name)
        user.activity = user_msg
        user.save()

    # list to store urls
    response.message("Your response has been saved")

    return HttpResponse(str(response))
