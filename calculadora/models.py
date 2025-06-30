from django.db import models

# Create your models here.

class Historial(models.Model):
    distancia = models.FloatField()
    frecuencia = models.FloatField()
    resultado = models.FloatField()

    def __str__(self):
        return f"{self.resultado:.2f} m"
