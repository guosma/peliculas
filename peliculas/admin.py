from django.contrib import admin
from peliculas.models import Pelicula, Director, Actor

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):

    def lista_actores(self, obj):
        ret = ''
        for actor in obj.actores.all()  :
            ret = ' {} {}'.format(ret, actor)

        return ret

    list_display = ['nombre', 'fecha_de_estreno', 'director', 'lista_actores']
    ordering = ['fecha_de_estreno']
    list_filter = ['director', 'actores']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido']
    ordering = ['apellido']


@admin.register(Actor)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido']
    ordering = ['apellido']