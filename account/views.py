from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(user.first_name)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        print(request.method)
        return render(request, 'index2.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password1 == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Alredy Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This Email ID is Registerd Alredy')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                user.save()
                messages.info(request, 'User Created')
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
    else:
        return render(request, 'register.html')
