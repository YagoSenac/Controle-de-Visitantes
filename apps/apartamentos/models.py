from django.db import models

# Create your models here.
class Apartamento(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    andar = models.IntegerField()
    garagem = models.BooleanField(default=False)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"Apartamento {self.numero} - Andar {self.andar}"

    class Meta:
        verbose_name = "Apartamento"
        verbose_name_plural = "Apartamentos"
        db_table = "Apartamento"