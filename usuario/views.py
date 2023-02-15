from django.shortcuts import render
from usuario.forms import LoginForm


def login(request):
    formulario = LoginForm()
    return render(request, "usuario/login.html", {"formulario": formulario})


def cadastro(request):
    return render(request, "usuario/cadastro.html")
