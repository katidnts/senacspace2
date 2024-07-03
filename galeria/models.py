from django.db import models

# Create your models here.

from django.db import models


class Fotografia(models.Model):
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galaxia"),
        ("PLANETA","Planeta")
    ]



    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=24, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%y/%m/%d", blank=True)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"


