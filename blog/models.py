from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField("Nombre", max_length=100)
    created = models.DateTimeField("Fecha de Creación", auto_now_add=True)
    updated = models.DateTimeField("Última Actualización", auto_now=True)
    
    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["name"]
        
    def __str__(self) -> str:
        return self.name.title()

class Post(models.Model):
    title= models.CharField("Título", max_length=100)
    content= models.TextField("Contenido")
    published= models.DateTimeField("Fecha de Publicación", default = timezone.now)
    image= models.ImageField("Imagen", upload_to="blog", null=True, blank=True)
    # OtO
    author=models.ForeignKey(User, models.CASCADE, verbose_name="Autor")
    categories = models.ManyToManyField(Category, "Categorías")
    created = models.DateTimeField("Fecha de Creación", auto_now_add=True)
    updated = models.DateTimeField("Última Actualización", auto_now=True)
    
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["-published"]
        
    def __str__(self) -> str:
        return self.title.title()