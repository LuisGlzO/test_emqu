from rest_framework import serializers
from .models import Usuario, Equipo, PruebaPing

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'correo']

class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'modelo', 'direccionIp']

class PruebaPingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaPing
        fields = ['id', 'fechaPrueba', 'equipo', 'usuario', 'respuesta']