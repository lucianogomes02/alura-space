from django.db import models
from enum import Enum
from datetime import datetime


class Categorias(Enum):
    NEBULOSA: str = "Nebulosa"
    ESTRELA: str = "Estrela"
    GALAXIA: str = "Galáxia"
    PLANETA: str = "Planeta"

    @classmethod
    def opcoes(cls):
        return [
            (cls.NEBULOSA.value, cls.NEBULOSA.value),
            (cls.ESTRELA.value, cls.ESTRELA.value),
            (cls.GALAXIA.value, cls.GALAXIA.value),
            (cls.PLANETA.value, cls.PLANETA.value),
        ]


class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    categoria = models.CharField(
        max_length=100, choices=Categorias.opcoes(), default=""
    )
    publicada = models.BooleanField(default=False)
    criada_em = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.nome
