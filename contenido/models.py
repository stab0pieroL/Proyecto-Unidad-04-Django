from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.

class Formulario(models.Model):
    titulo= CharField(max_length=100)
    descripcion= CharField(max_length=300)
    imagen = ImageField(upload_to="portoflio/images")
    url = URLField(blank=True)
    tags = CharField(max_length=30)