from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def registro(request):
    return render(request, "registro.html",
                   {"form": UserCreationForm})

def home (request):
    return render(request,"home.html")

def signup(request) :
    if request.method == "GET":
        return render(request, "singup.html",
                    {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try: 
                user = User.objects.create_user(request.POST['username'], 
                                                password=request.POST['password1'])
                user.save()
                return HttpResponse("Usuario creado correctamente")
            except: 
                return HttpResponse("Error al crear el usuario")   
        else:
            return HttpResponse("Las contraseñas no coinciden") 

 