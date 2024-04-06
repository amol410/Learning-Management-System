from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django. contrib import messages
from app.EmailBackend import EmailBackEnd
from django.contrib.auth import authenticate, login, logout


def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username') # name = username (coming from http template)
        email = request.POST.get('email')  # email = email (coming from http template)       
        password = request.POST.get('password') # password = password (coming from http template)

        if User.objects.filter(email=email).exists():
           messages.warning(request, 'Email are Already Exists !')
           return redirect ('register')
    
        if User.objects.filter(username=username).exists():
           messages.warning(request, 'Username are Already Exists !')
           return redirect ('register')
    
        user = User(
                username=username,
                email=email,)
        user.set_password(password)
        user.save()
        return redirect('login')

    
    return render(request, 'registration/register.html')

def DO_LOGIN(request):
    if request.method == "POST":
        email = request.POST.get('email')  # email = email (coming from http template)       
        password = request.POST.get('password') # password = password (coming from http template)
        

        user = EmailBackEnd.authenticate(request, username=email, password=password)

        if user != None:
           login(request, user)
           return redirect('home')
        
        else:
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')

    return None

def PROFILE (request):
    return render(request, 'registration/profile.html')

def PROFILE_UPDATE(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')

        
    return None