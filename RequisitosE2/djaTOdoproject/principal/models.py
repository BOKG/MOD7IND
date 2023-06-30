from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField(default=datetime.now, blank=True)
    STATUS_CHOICES = (
        ('P', 'Pendiente'),
        ('IP', 'En progreso'),
        ('C', 'Completada'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    label = models.ForeignKey('Label', on_delete=models.CASCADE)


class Label(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre