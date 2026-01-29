from django import forms
from django.forms import inlineformset_factory
from volley_team_maker.models import Equipo, Jugador, EstadisticasJugador, Partido



class StatsEditables(forms.ModelForm):
    class Meta:
        model = EstadisticasJugador
        fields = ('position1', 'position2', 'height', 'saque', 'recepcion', 'dedos', 'dedos_doble', 'ataque', 'foto',)

class EstadisticasJugadorForm(forms.ModelForm):
    class Meta:
        model = EstadisticasJugador
        fields = ('position1', 'position2', 'height', 'saque', 'recepcion', 'dedos', 'dedos_doble', 'ataque')


class EquipoPartidoEditable(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ('equipo', 'partido',)


class JugadorForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'rut','genero')
        model = Jugador

class EquipoForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'max_num_players')
        model = Equipo




class FormularioJugador(forms.ModelForm):
    class Meta:
        fields = ('name', 'rut', 'genero',)
        model = Jugador

class FormularioJugador2(forms.ModelForm):
    class Meta:
        fields = ('height', 'position1', 'position2',)
        model = EstadisticasJugador
class FechaEditable(forms.ModelForm):
    class Meta:
        fields = ('fecha',)
        model = Partido

class EstadoEditable(forms.ModelForm):
    class Meta:
        fields = ('status',)
        model = Partido

class NumplayersEditable(forms.ModelForm):
    class Meta:
        fields = ('num_players',)
        model = Partido


