from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia


def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    fotografias = Fotografia.objects.order_by("criada_em").filter(publicada=True)
    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, id_foto):
    fotografia = get_object_or_404(Fotografia, pk=id_foto)
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        return redirect("login")

    fotografias = Fotografia.objects.order_by("criada_em").filter(publicada=True)
    if "buscar" in request.GET:
        nome = request.GET.get("buscar")
        if nome:
            fotografias = fotografias.filter(nome__icontains=nome)
    return render(request, "galeria/buscar.html", {"cards": fotografias})
