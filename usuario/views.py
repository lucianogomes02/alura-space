from django.shortcuts import render, redirect
from usuario.forms import LoginForm, CadastroForm

from django.contrib.auth.models import User


def login(request):
    formulario = LoginForm()
    return render(request, "usuario/login.html", {"formulario": formulario})


def cadastro(request):
    formulario = CadastroForm()

    if request.method == "POST":
        formulario = CadastroForm(request.POST)

        if formulario.is_valid():
            nome_de_cadastro = formulario["nome_de_cadastro"].value()
            email = formulario["email"].value()
            senha = formulario["senha"].value()
            confirmacao_de_senha = formulario["confirmacao_de_senha"].value()

            usario_ja_existe = User.objects.filter(username=nome_de_cadastro).exists()

            if senha != confirmacao_de_senha or usario_ja_existe:
                return redirect("cadastro")

            usuario = User.objects.create_user(
                username=nome_de_cadastro, email=email, password=senha
            )
            usuario.save()
            return redirect("login")
    return render(request, "usuario/cadastro.html", {"formulario": formulario})
