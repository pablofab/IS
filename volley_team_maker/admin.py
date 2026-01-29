from django.contrib import admin

from .models import Equipo, EstadisticasJugador, Jugador, Partido, User

admin.site.register(Equipo)
admin.site.register(Partido)
admin.site.register(Jugador)
admin.site.register(EstadisticasJugador)
admin.site.register(User)