from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login,logout

from volley_team_maker.forms import StatsEditables, EquipoPartidoEditable, EquipoForm
from volley_team_maker.models import Jugador, EstadisticasJugador, User, Equipo
from volley_team_maker.forms import FormularioJugador, FormularioJugador2
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def register_user(request):
    if request.method == 'GET':
        return render(request,"volley_team_maker/register_user.html",{})
    elif request.method == 'POST':
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        mail = request.POST['mail']
        user = User.objects.create_user(username=nombre, email=mail, password=contraseña, role=2)
        messages.success(request, 'Se creó el usuario ' + user.username)
        return HttpResponseRedirect('/inicio')

def user_register(request):
    if request.method == "GET":
        form1 = JugadorForm()
        form2 = EstadisticasJugadorForm()
        return render(request, "volley_team_maker/register_user.html", {"form1": form1, "form2": form2})
    if request.method == "POST":
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        mail = request.POST['mail']
        user = User.objects.create_user(username=nombre, email=mail, password=contraseña, role=2)
        jugador_form = JugadorForm(request.POST)
        estadisticas_jugador_form = EstadisticasJugadorForm(request.POST)
        if jugador_form.is_valid() and estadisticas_jugador_form.is_valid():
            estadisticas_jugador = estadisticas_jugador_form.save()
            jugador_form.instance.estadisticas_jugador = estadisticas_jugador
            jugador = jugador_form.save()
            user.jugador = jugador
            user.save()
        messages.success(request, 'Se creó el usuario ' + user.username)    
        return HttpResponseRedirect('/inicio')


def login_user(request):
    if request.method == 'GET':
        return render(request, "volley_team_maker/login_user.html",{})
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña) 
        if usuario is not None:
            login(request, usuario)
            if request.user.role == 2:
                messages.success(request, 'Te damos la bienvenida ' + username)
                return HttpResponseRedirect('/inicio')
            else:
                logout(request)
                messages.success(request, 'Usuario incorrecto')
                return HttpResponseRedirect('/login')     
        else:
            messages.success(request, 'Usuario incorrecto')
            return HttpResponseRedirect('/login')           

def login_adminuser(request):
    if request.method == 'GET':
        return render(request, "volley_team_maker/login_adminuser.html",{})
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request, usuario)
            if request.user.role == 1:
              messages.success(request, 'Te damos la bienvenida admin ' + username)
              return HttpResponseRedirect('/inicio')
            else:
              logout(request)
              messages.success(request, 'Usuario admin incorrecto')
              return HttpResponseRedirect('/adminlogin')    
        else:
            messages.success(request, 'Usuario admin incorrecto')
            return HttpResponseRedirect('/adminlogin')  

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/inicio')  

def voleibol(request):
    mi_voleibol = Jugador.objects.all()

    if request.method == "GET":
        return render(request, "volley_team_maker/home.html", {"voleibol": mi_voleibol})


def lista_Jugadores(request):
    jugadores = Jugador.objects.all()
    users = User.objects.all()
    return render(request, "volley_team_maker/ListaJugadores.html", {"jugadores": jugadores, "users": users})

def lista_Jugadores2(request):
    jugadores = Jugador.objects.all()
    return render(request, "volley_team_maker/ListaJugadores2.html", {"jugadores": jugadores})

def crear_equipo(request):
    if request.method == 'GET':
        return render(request,"volley_team_maker/equipos.html",{})

    elif request.method == 'POST':
        nombre = request.POST['nombre']
        equipo = Equipo.objects.create(name=nombre)
        messages.success(request, 'Se creó un nuevo equipo')
        return HttpResponseRedirect('/equipos')

def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, "volley_team_maker/equipos.html", {"equipos": equipos} )

def view_equipo(request,id_equipo):
    equipo = Equipo.objects.get(pk=id_equipo)
    jugadores = equipo.jugador_set.all()
    return render(request, 'volley_team_maker/equipo_players.html', {"equipo": equipo, "jugadores": jugadores})

def view_jugador(request, id_jugador):
    jugador = Jugador.objects.get(pk=id_jugador)
    stats = EstadisticasJugador.objects.get(pk=id_jugador)
    return render(request, 'volley_team_maker/viewJugador.html', {'jugador' : jugador, "stats" : stats})

def view_my_profile(request, id_user):
    jugador = Jugador.objects.get(pk=id_user)
    stats = EstadisticasJugador.objects.get(pk=id_user)
    return render(request, 'volley_team_maker/viewJugador.html', {'jugador' : jugador, "stats" : stats})

def equipo_jugadores_disponibles(request, id_equipo):
    equipo = Equipo.objects.get(pk=id_equipo)
    # Jugadores sin equipo
    jugadores = Jugador.objects.filter(equipo__isnull=True)
    return render(request, 'volley_team_maker/equipo_add_player.html', {"equipo": equipo, "jugadores": jugadores})

def equipo_remover_jugador(request,id_equipo,id_jugador):
    jugador = Jugador.objects.get(pk=id_jugador)
    equipo = Equipo.objects.get(pk=id_equipo)
    equipo.jugador_set.remove(jugador)
    equipo.num_players = equipo.num_players - 1
    equipo.save()
    return HttpResponseRedirect('/equipos/' + str(id_equipo))

def equipo_agregar_jugador(request, id_equipo,id_jugador):
    jugador = Jugador.objects.get(pk=id_jugador)
    equipo = Equipo.objects.get(pk=id_equipo)
    equipo.jugador_set.add(jugador)
    equipo.num_players = equipo.num_players + 1
    equipo.save()
    return HttpResponseRedirect('/equipos/' + str(id_equipo) + '/jugadoresDisponibles')

def equipo_estadisticas(request, id_equipo): 
    equipo = Equipo.objects.get(pk=id_equipo)
    jugadores = Jugador.objects.filter(equipo=equipo)
    return render(request, 'volley_team_maker/equipo_estadisticas.html', {"equipo": equipo, "jugadores": jugadores})

def equipo_registrar(request):
    if request.method == "GET":
        form1 = EquipoForm()
        return render(request, "volley_team_maker/equipo_register.html", {"form1": form1})
    if request.method == "POST":
        form1 = EquipoForm(request.POST)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect('/equipos')

def equipo_editar(request, id_equipo):
    equipo = Equipo.objects.get(pk=id_equipo)
    if request.method == "GET":
        form1 = EquipoForm(instance=equipo)
        return render(request, "volley_team_maker/equipo_edit.html", {"form1": form1, "equipo": equipo})
    if request.method == "POST":
        form1 = EquipoForm(request.POST, instance=equipo)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect('/equipos')



def edit(request, id_jugador):
    jugador = EstadisticasJugador.objects.filter(id=id_jugador).first()
    form = StatsEditables(instance=jugador)
    return render(request, "volley_team_maker/JugadorEdit.html", {"form": form, "jugador": jugador})


def edit2(request, id_jugador):
    jugador = Jugador.objects.filter(id=id_jugador).first()
    form2 = EquipoPartidoEditable(instance=jugador)
    return render(request, "volley_team_maker/EquipoEdit.html", {"form": form2, "jugador": jugador})


def actualizar_jugador(request, id_jugador):
    jugador = EstadisticasJugador.objects.get(pk=id_jugador)
    form = StatsEditables(request.POST, request.FILES, instance=jugador)
    if form.is_valid():
        form.save()
    jugadores = Jugador.objects.all()
    return render(request, "volley_team_maker/ListaJugadores.html", {"form": form, "jugadores": jugadores})


def actualizar_jugador2(request, id_jugador):
    jugador = Jugador.objects.get(pk=id_jugador)
    form = EquipoPartidoEditable(request.POST, instance=jugador)
    if form.is_valid():
        form.save()
    jugadores = Jugador.objects.all()
    return render(request, "volley_team_maker/ListaJugadores.html", {"form": form, "jugadores": jugadores})


def eliminar(request, id_jugador):
    jugador = Jugador.objects.get(pk=id_jugador)
    stats = EstadisticasJugador.objects.get(pk=id_jugador)
    if request.method == "POST":
        jugador.delete()
        stats.delete()
        return redirect("../listaJugadores/")
    return render(request, "volley_team_maker/ConfirmarEliminacion.html", {"jugador": jugador, "mensaje": 'OK'})

def jugador_registrar(request):
    if request.method == "GET":
        form1 = JugadorForm()
        form2 = EstadisticasJugadorForm()
        return render(request, "volley_team_maker/jugador_add.html", {"form1": form1, "form2": form2})
    if request.method == "POST":
        jugador_form = JugadorForm(request.POST)
        estadisticas_jugador_form = EstadisticasJugadorForm(request.POST)
        if jugador_form.is_valid() and estadisticas_jugador_form.is_valid():
            estadisticas_jugador = estadisticas_jugador_form.save()
            jugador_form.instance.estadisticas_jugador = estadisticas_jugador
            jugador_form.save()
            return HttpResponseRedirect('/listaJugadores2')




def jugador_editar(request, id_jugador):
    jugador = Jugador.objects.get(pk=id_jugador)
    estadisticas_jugador = EstadisticasJugador.objects.get(pk=id_jugador)

    if request.method == "GET":
        jugador_form = JugadorForm(instance=jugador)
        estadisticas_jugador_form = EstadisticasJugadorForm(instance=estadisticas_jugador)
        return render(request, "volley_team_maker/jugador_editar.html", {"estadisticas_jugador_form": estadisticas_jugador_form, "jugador": jugador, "jugador_form" :jugador_form})
    if request.method == "POST":
        jugador_form = JugadorForm(request.POST)
        estadisticas_jugador_form = EstadisticasJugadorForm(request.POST, instance=estadisticas_jugador)
        if jugador_form.is_valid():
            jugador_form.save()
        jugadores = Jugador.objects.all()
        return render(request, "volley_team_maker/jugador_editar.html", {"jugadores": jugadores})

def crear_partido(request):
    if request.method == 'GET':
        return render(request,"volley_team_maker/partidos.html",{})

    elif request.method == 'POST':
        partido = Partido.objects.create()
        messages.success(request, 'Se creó un nuevo partido')
        return HttpResponseRedirect('/partidos')


def listar_partidos(request):
    partidos = Partido.objects.all()
    return render(request, "volley_team_maker/partidos.html", {"partidos": partidos} )


def view_partido(request,id_partido):
    partido = Partido.objects.get(pk=id_partido)
    equipos = partido.equipo_set.all()
    return render(request, 'volley_team_maker/partido_teams.html', {"partido": partido, "equipos": equipos})


def partido_equipos_disponibles(request, id_partido):
    partido = Partido.objects.get(pk=id_partido)
    # Equipos sin partido
    equipos = Equipo.objects.filter(partido__isnull=True)
    return render(request, 'volley_team_maker/partido_add_team.html', {"partido": partido, "equipos": equipos})


def partido_agregar_equipo(request, id_partido,id_equipo):
    equipo = Equipo.objects.get(pk=id_equipo)
    partido = Partido.objects.get(pk=id_partido)
    partido.equipo_set.add(equipo)
    partido.num_players = partido.num_players + equipo.num_players
    partido.save()
    return HttpResponseRedirect('/partidos/' + str(id_partido) + '/equiposDisponibles')


def partido_remover_equipo(request,id_partido,id_equipo):
    equipo = Equipo.objects.get(pk=id_equipo)
    partido = Partido.objects.get(pk=id_partido)
    partido.equipo_set.remove(equipo)
    return HttpResponseRedirect('/partidos/' + str(id_partido))


def editFecha(request, id_partido):
    partido = Partido.objects.filter(id=id_partido).first()
    formFecha = FechaEditable(instance=partido)
    return render(request, "volley_team_maker/partido_edit_date.html", {"form": formFecha, "partido": partido})


def actualizar_fecha(request, id_partido):
    partido = Partido.objects.get(pk=id_partido)
    form = FechaEditable(request.POST, instance=partido)
    if form.is_valid():
        form.save()
    partidos = Partido.objects.all()
    return render(request, "volley_team_maker/partidos.html", {"form": form, "partidos": partidos})



def editEstado(request, id_partido):
    partido = Partido.objects.filter(id=id_partido).first()
    formEstado = EstadoEditable(instance=partido)
    return render(request, "volley_team_maker/partido_edit_status.html", {"form": formEstado, "partido": partido})


def actualizar_estado(request, id_partido):
    partido = Partido.objects.get(pk=id_partido)
    form = EstadoEditable(request.POST, instance=partido)
    if form.is_valid():
        form.save()
    partidos = Partido.objects.all()
    return render(request, "volley_team_maker/partidos.html", {"form": form, "partidos": partidos})



def editNumplayers(request, id_partido):
    partido = Partido.objects.filter(id=id_partido).first()
    formNumplayers = NumplayersEditable(instance=partido)
    return render(request, "volley_team_maker/partido_edit_numplayers.html", {"form": formNumplayers, "partido": partido})

def actualizar_numplayers(request, id_partido):
    partido = Partido.objects.get(pk=id_partido)
    form = NumplayersEditable(request.POST, instance=partido)
    if form.is_valid():
        form.save()
    partidos = Partido.objects.all()
    return render(request, "volley_team_maker/partidos.html", {"form": form, "partidos": partidos})



def partido_jugadores(request, id_equipo):
    equipo = Equipo.objects.get(pk=id_equipo)
    jugadores = Jugador.objects.filter(equipo=equipo)
    return render(request, 'volley_team_maker/partido_players.html', {"equipo": equipo, "jugadores": jugadores})









@cache_page(60 * 15)
@csrf_protect
def buscar(request):
    if request.method == "POST":
        buscarJugador = request.POST['buscarJugador']
        jugadores = Jugador.objects.filter(name__contains= buscarJugador)
        return render(request, "volley_team_maker/BuscarJugadores.html", {"buscarJugador": buscarJugador, "jugadores": jugadores})
    else:
        return render(request, "volley_team_maker/BuscarJugadores.html", {})




def Jugadores(request):
    mi_jugador = Jugador.objects.all()
    mis_estadisticas = EstadisticasJugador.objects.all()

    if request.method == "POST":
        nombre = request.POST.get('name')
        rut = request.POST["rut"]
        genero = request.POST["genero"]
        estatura = request.POST["height"]
        position1 = request.POST["position1"]
        position2 = request.POST["position2"]

        mi_jugador = Jugadores(name=nombre, rut=rut, genero=genero, height=estatura, position1=position1, position2=position2)
        mi_jugador.save()

    return render(request, "volley_team_maker/jugadores.html",
                  {"jugadores": mi_jugador, "estadisticas": mis_estadisticas})


class FormularioJugadorView(HttpRequest):
    def index(request):
        form1 = FormularioJugador()
        form2 = FormularioJugador2()
        return render(request, "volley_team_maker/form.html", {"form1": form1, "form2": form2})

    def procesar_formulario(request):

        if request.method == 'POST':
            form1 = FormularioJugador(request.POST)
            form2 = FormularioJugador2(request.POST)
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                return render(request, "volley_team_maker/success.html")
            else:
                context = {
                    'form1': form1,
                    'form2': form2,
                }
        else:
            context = {
                'form1': FormularioJugador(),
                'form2': FormularioJugador2(),
            }

        return render(request, 'volley_team_maker/form.html', context)





