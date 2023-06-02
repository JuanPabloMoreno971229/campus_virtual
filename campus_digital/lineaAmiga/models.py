from django.db import models

# Create your models here.

class LineaAmiga(models.Model):
    
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    image= models.ImageField(verbose_name="Imagen", upload_to="linea amiga")
    question1 = models.TextField(verbose_name="Pregunta 1")
    question2 = models.TextField(verbose_name="Pregunta 2")
    question3 = models.TextField(verbose_name="Pregunta 3")
    question4 = models.TextField(verbose_name="Pregunta 4")
    link_date = models.URLField(verbose_name="Link agendar cita")
    link_FQ = models.URLField(verbose_name="Link preguntas frecuentes")
    

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural = "Contenidos"
    def __str__(self):
        return self.title