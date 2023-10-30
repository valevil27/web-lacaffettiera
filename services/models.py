from django.db import models 
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
    title = models.CharField("Título", max_length= 200)
    subtitle = models.CharField("Subtítulo", max_length= 200)
    content = RichTextField("Contenido")
    image = models.ImageField("Imagen", upload_to='services')
    created = models.DateTimeField("Fecha de Creación", auto_now_add=True)
    updated = models.DateTimeField("Última Actualización", auto_now=True)
    
    def __str__(self):
        return self.title.title()
    
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]
