from django.shortcuts import render
from rest_framework.views import APIView
from .models import Usuario, Equipo, PruebaPing
from .serielizers import UsuarioSerializer, EquipoSerializer, PruebaPingSerializer
from rest_framework.response import Response
from rest_framework import status
import random

# Create your views here.
class UsuarioApi(APIView):
    def get(self, request, format=None):
        equipos = Usuario.objects.all()
        serializer = UsuarioSerializer(equipos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):
    def get(self, request, usuario_id):
        usuario = Usuario.objects.get(id=usuario_id)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    
    def put(self, request, usuario_id):
        usuario = Usuario.objects.get(id=usuario_id)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, usuario_id):
        usuario = Usuario.objects.get(id=usuario_id)
        usuario.delete()
        return Response({"message" :" Usuario eliminado"}, status=status.HTTP_200_OK)

class EquipoApi(APIView):
    def get(self, request, format=None):
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EquipoDetail(APIView):
    def get(self, request, equipo_id):
        usuario = Equipo.objects.get(id=equipo_id)
        serializer = EquipoSerializer(usuario)
        return Response(serializer.data)
    
    def put(self, request, equipo_id):
        usuario = Equipo.objects.get(id=equipo_id)
        serializer = EquipoSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, equipo_id):
        usuario = Equipo.objects.get(id=equipo_id)
        usuario.delete()
        return Response({"message" :" Equipo eliminado"}, status=status.HTTP_200_OK)

class PruebaPingApi(APIView):
    def get(self, request, format=None):
        pruebas = PruebaPing.objects.all()
        print(pruebas)
        serializer = PruebaPingSerializer(pruebas, many=True)
        return Response(serializer.data)

    def post(self, request):
        respuestaPosible = ['1', '2', '3', '4', '5']
        """
        Si la respuesta es del 1 al 3, entonces decimos que el equipo responden,
        si la respuesta es 4 o 5 entonces el equipo no responde
        """
        respuesta = random.choice(respuestaPosible)
        #print(request.data['usuario'])
        print(respuesta)
        if respuesta != '4' and respuesta != '5':
            request.data['respuesta'] = 'Y'
        else:
            request.data['respuesta'] = 'N'
        serializer = PruebaPingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)