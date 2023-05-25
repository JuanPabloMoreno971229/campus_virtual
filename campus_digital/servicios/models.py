from django.db import models

# Create your models here.

class Services(models.Model):
    title= models.CharField(max_length=200, verbose_name="Título")
    subtitle= models.CharField(max_length=200, verbose_name="Subtitulo")
    description= models.TextField(verbose_name="Descripción")
    image= models.ImageField(verbose_name="Imagen banner", upload_to="projects")
    category=models.CharField(max_length=200, null=True, verbose_name="Categoría", choices= (
        ('P', 'Pregrado'),
        ('G', 'Postgrado'),
        ('A', 'Ambos'),
        ('D', 'Administrativos'),
        ('T', 'Todos'),
    ))
    image_2= models.ImageField(verbose_name="Imagen", upload_to="projects")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"]
    def __str__(self):
        return self.category