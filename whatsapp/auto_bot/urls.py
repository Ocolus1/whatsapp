from django.urls import path
from .views import *

app_name = "auto_bot"
urlpatterns = [
	#Leave as empty string for base url
	path('twilo/', index, name="index"),
]
