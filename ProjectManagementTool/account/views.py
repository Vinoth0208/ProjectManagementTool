from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import User


# Create your views here.
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)

                return redirect('/')

    return render(request, 'account/signin.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password1 = request.POST.get('password1', '')

        if username and email and password and password1:

            user = User.objects.create_user(username, email, password)
            print('User Created: ', user)

            return redirect('/signin/')
        else:
            print('Something went wrong')
    else:
        print('Just show the form!')
    return render(request, 'account/signup.html')

