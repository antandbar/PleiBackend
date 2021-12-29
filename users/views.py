from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout as django_logout, authenticate, login as django_login


def login(request):
    error_messages = []
    if request.method == 'POST':
        username = request.POST.get['usr']
        password = request.POST.get['pwd']
        user = authenticate(username=username, password=password)
        if user is None:
            error_messages.append('Nombre de usuario o contraseña incorrectos')
        else:
            if user.is_active:
                django_login(request, user)
            else:
                error_messages.append('el usuario no está activo')


    documento = "<HTML><body><h1>hola mundo</h1></body></HTML>"
    return HttpResponse(documento)


def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    documento = "<HTML><body><h1>hola mundo</h1></body></HTML>"
    return HttpResponse(documento)

