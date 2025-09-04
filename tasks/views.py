from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


# Create your views here.
def home(request):
    return render(request, "home.html")
def signout(request):
     logout(request)
     return redirect("home")

def tasks(request):
    return render(request, "tasks.html")

def signin(request):
     if request.method == "GET":
          return render(request,
                        "signin.html",
                        {"form":AuthenticationForm()})
     else:
        user = authenticate(request,
                             username=request.POST.get('username'),
                             password=request.POST.get('password'))
        
        if user is None:
             return render(request,
                              "signin.html",
                              {"form":AuthenticationForm(),
                              "error":"Usuario o contraseña incorrecta"})
        else:
                 login(request, user)
                 return redirect("tasks")
                

def signup(request):
    if request.method == "GET":
        return render(request, 
                  "signup.html",
                  {"form":UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("tasks")

            except IntegrityError:
                return render(request,
                              'signup.html',
                              {"form": UserCreationForm(),
                               "error":"Error al crear el usuario"})
                
        else:
                 return render(request,
                              'signup.html',
                              {"form": UserCreationForm(),
                               "error":"Error Las contraseñas no coinciden"})