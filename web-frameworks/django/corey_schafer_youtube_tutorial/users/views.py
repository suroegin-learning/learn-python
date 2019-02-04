from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            confirmed_password = form.cleaned_data.get('password2')
            agree_with_terms = form.cleaned_data.get('agree_with_terms')

            print(f'Account created for {username} with email: {email} and password: {password}!')
            messages.success(request, f'Account created for {username} with email: {email} and password: {password}!')
            return redirect('homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

