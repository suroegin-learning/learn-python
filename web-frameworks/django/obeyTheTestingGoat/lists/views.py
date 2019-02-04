from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item


def home_page(request):
    if request.method == "POST":
        new_item_text = request.POST["item_text"]
        print(new_item_text)
        try:
            Item.objects.create(text=new_item_text)
        except Exception as e:
            print(e)

        return redirect('/')
    else:
        items = Item.objects.all()

    return render(request, 'home.html', {
        'items': items
    })
