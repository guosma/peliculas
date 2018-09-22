from django.contrib import admin
from alquileres.models import AlquilerPelicula, Alquiler


class AlquilerPeliculaInline(admin.StackedInline):
    model = AlquilerPelicula
    extras = 3 

@admin.register(Alquiler)
class AlquilerAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'momento']
    inlines = [AlquilerPeliculaInline]
