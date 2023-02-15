from django.shortcuts import render
from usuario.forms import LoginForm, CadastroForm


def login(request):
    formulario = LoginForm()
    return render(request, "usuario/login.html", {"formulario": formulario})


def cadastro(request):
    formulario = CadastroForm()
    return render(request, "usuario/cadastro.html", {"formulario": formulario})
