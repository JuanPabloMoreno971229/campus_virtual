from django.db import models

# Create your models here.

class LineaAmiga(models.Model):
    
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    image= models.ImageField(verbose_name="Imagen", upload_to="linea amiga")
    

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural = "Contenidos"
    def __str__(self):
        return self.title