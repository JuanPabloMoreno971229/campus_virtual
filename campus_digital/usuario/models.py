from django.db import models

# Create your models here.

class User(models.Model):
    ID=models.AutoField(verbose_name="ID", primary_key=True)
    name= models.CharField(max_length=200, verbose_name="Nombre")
    program= models.CharField(max_length=200, verbose_name="Programa")
    user= models.CharField(max_length=200, verbose_name="Usuario")
    password= models.CharField(max_length=200, verbose_name="Contraseña")
    image= models.ImageField(verbose_name="Foto de perfil", upload_to="projects")
    category=models.CharField(max_length=200, null=True, verbose_name="Categoría", choices= (
        ('P', 'Pregrado'),
        ('G', 'Postgrado'),
        ('A', 'Ambos'),
        ('D', 'Administrativos'),
        ('T', 'Todos'),
    ))
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-created"]
    def __str__(self):
        return self.category