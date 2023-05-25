from django.db import models

class Ruta(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)

class Horario(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    hora_salida = models.DateTimeField()
    asientos_disponibles = models.IntegerField()

class Reserva(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    nombre_pasajero = models.CharField(max_length=100)
    numero_asiento = models.IntegerField()
