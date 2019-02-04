from django.shortcuts import render
from .models import *


def homepage(request):
    posts = Post.objects.all()
    return render(request, "main/homepage.html", {'posts': posts})