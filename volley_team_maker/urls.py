from django.urls import path
from . import views


urlpatterns = [
    path('myProfile/<int:id_user>', views.view_my_profile, name='my_profile'),
    path('voleibol', views.voleibol, name= 'my_volleyball'),
    path('inicio/', views.voleibol, name= 'inicio'),
    path("listaJugadores/", views.lista_Jugadores, name='listaJugadores'),
    path("listaJugadores2/", views.lista_Jugadores2, name='listaJugadores2'),
    path("editarJugadores/<int:id_jugador>", views.edit, name='editarJugadores'),
    path("editarEquipoPartido/<int:id_jugador>", views.edit2, name='editarJugadores2'),
    path("actualizarJugador/<int:id_jugador>", views.actualizar_jugador, name='actualizarJugador'),
    path("actualizarJugador2/<int:id_jugador>", views.actualizar_jugador2, name='actualizarJugador2'),
    path("eliminarJugador/<int:id_jugador>", views.eliminar, name='eliminarJugador'),
    path("buscarJugador/", views.buscar, name='buscarJugador'),
    path('jugadores/', views.jugador_registrar, name='mi_jugador'),
    path('success/', views.FormularioJugadorView.procesar_formulario, name='success'),
    path('home/', views.voleibol, name= 'home'),
    path('equipos/', views.listar_equipos, name='equipos'),
    path('crearEquipo/', views.crear_equipo, name='crearEquipo'),
    path('equipos/<int:id_equipo>', views.view_equipo, name='equipo'),
    path('equipos/registrar', views.equipo_registrar, name='equipo_registrar'),
    path('equipos/<int:id_equipo>/editar', views.equipo_editar, name='equipo_editar'),
    path('equipos/<int:id_equipo>/jugadoresDisponibles', views.equipo_jugadores_disponibles, name='equipo_jugadores_disponibles'),
    path('equipos/<int:id_equipo>/agregarJugador/<int:id_jugador>', views.equipo_agregar_jugador, name='equipo_agregar_jugador'),
    path('equipos/<int:id_equipo>/removerJugador/<int:id_jugador>', views.equipo_remover_jugador, name='equipo_remover_jugador'),
    path('equipos/<int:id_equipo>/estadisticas', views.equipo_estadisticas, name='equipo_estadisticas'),
    path('partidos/', views.listar_partidos, name='partidos'),
    path('crearPartido/', views.crear_partido, name='crearPartido'),
    path('partidos/<int:id_partido>', views.view_partido, name='partido'),
    path('partidos/<int:id_partido>/equiposDisponibles', views.partido_equipos_disponibles, name='partido_equipos_disponibles'),
    path('partidos/<int:id_partido>/agregarEquipo/<int:id_equipo>', views.partido_agregar_equipo, name='partido_agregar_equipo'),
    path('partidos/<int:id_partido>/removerEquipo/<int:id_equipo>', views.partido_remover_equipo, name='partido_remover_equipo'),
    path('equipos/<int:id_equipo>/jugadores', views.partido_jugadores, name='partido_jugadores'),
    path("editarFecha/<int:id_partido>", views.editFecha, name='editarFecha'),
    path("actualizarFecha/<int:id_partido>", views.actualizar_fecha, name='actualizarFecha'),
    path("editarEstado/<int:id_partido>", views.editEstado, name='editarEstado'),
    path("actualizarEstado/<int:id_partido>", views.actualizar_estado, name='actualizarEstado'),
    path("editarNumplayers/<int:id_partido>", views.editNumplayers, name='editarNumplayers'),
    path("actualizarNumplayers/<int:id_partido>", views.actualizar_numplayers, name='actualizarNumplayers'),
    path('adminlogin/', views.login_adminuser, name= 'adminlogin'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.user_register, name='register_user'),
    path('viewJugador/<int:id_jugador>', views.view_jugador, name= 'view_jugador'),
    path('login', views.login_user, name = 'login'),

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
