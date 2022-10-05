import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('start')
        else:
            messages.info(request, 'Invalid login or password!')
            return redirect('home')

    else:
        return render(request, 'home.html')
@login_required(login_url='/')
def start(request):
    return render(request, 'start.html')
@login_required(login_url='/')
def logoutUser(request):
    logout(request)
    return redirect('home')
def registerUser(request):
    return render(request, 'register.html')
def registerUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'Successfully registered.')
                return redirect('home')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
        
    else:
        return render(request, 'register.html')