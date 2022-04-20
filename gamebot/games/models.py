from tabnanny import verbose
from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200,unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        ordering = ['name']