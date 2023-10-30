from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField("Título", max_length=100)
    content = models.TextField("Contenido")
    created = models.DateTimeField("Fecha de Creación", auto_now_add=True)
    updated = models.DateTimeField("Última Actualización", auto_now = True)

    class Meta:
        verbose_name = "página"
        ordering = ("title",)
    
    def __str__(self) -> str:
        return self.title.title()