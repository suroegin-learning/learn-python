from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from background_task import background


@background(schedule=3)
def callback(user):
    user = User.objects.get(pk=user)
    print(user.username)


def index(request):
    callback(request.user.id)
    return HttpResponse("OK")
