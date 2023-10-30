from django.db import models

# Create your models here.
class Link(models.Model):
    # Slug -> Normalized text
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField("Red social", max_length=200)
    url = models.URLField("Enlace", max_length=200, blank=True, null=True)
    created = models.DateTimeField("Fecha de Creación", auto_now_add=True)
    updated = models.DateTimeField("Última Actualización", auto_now=True)
    
    class Meta:
        verbose_name="link"
        ordering = ("name",)