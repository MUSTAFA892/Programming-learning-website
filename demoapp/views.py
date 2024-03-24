from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Me

def index(request):
    return render(request, 'index.html')

def Mess(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        my_mess = Me.objects.create(name=name, email=email)
        my_mess.save()
        messages.success(request, 'Message sent successfully!')
        return redirect('index')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('index')
