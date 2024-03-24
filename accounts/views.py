from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return redirect('register')
        else:
            my_user = User.objects.create_user(username=email, email=email, password=pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        mail = request.POST.get('email')
        passw = request.POST.get('password')
        my_user = authenticate(request, email= mail, password=passw)
        if my_user is not None:
            login(request, my_user)
            return redirect("index")
        else:
            return redirect("index")
    return render(request, 'login.html')
