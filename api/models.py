from django.db import models

# Create your models here.
class Usuario(models.Model):
    #id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 200)

    def __str__(self):
        persona = self.nombre + ' ' + self.apellido
        return persona

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    direccionIp = models.CharField(max_length=15)
    def __str__(self):
        return self.nombre

class PruebaPing(models.Model):
    fechaPrueba = models.DateTimeField(auto_now_add=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=1)