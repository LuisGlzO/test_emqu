from django.contrib import admin
from .models import Usuario, Equipo, PruebaPing

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class EquipoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class PruebaAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'fechaPrueba')

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(PruebaPing, PruebaAdmin)