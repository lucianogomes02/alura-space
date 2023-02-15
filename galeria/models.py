from django.db import models
from enum import Enum


class Categorias(Enum):
    NEBULOSA: str = "Nebulosa"
    ESTRELA: str = "Estrela"
    GALAXIA: str = "Galáxia"
    PLANETA: str = "Planeta"

    @classmethod
    def opcoes(cls):
        return [
            ("NEBULOSA", cls.NEBULOSA.value),
            ("ESTRELA", cls.ESTRELA.value),
            ("GALÁXIA", cls.GALAXIA.value),
            ("PLANETA", cls.PLANETA.value),
        ]


class Fotografia(models.Model):
    OPCOES_DE_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(
        max_length=100, choices=Categorias.opcoes(), default=""
    )

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
