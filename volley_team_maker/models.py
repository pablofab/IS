from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser



class Partido(models.Model):
    EN_PREPARACION = 'En preparacion'
    ESPERA = 'Espera'
    LISTO = 'Listo'

    STATES = (
        (EN_PREPARACION, EN_PREPARACION),
        (ESPERA, ESPERA),
        (LISTO, LISTO),
    )
    # Fields
    fecha = models.DateTimeField(max_length=255, default="2012-12-31")
    status = models.CharField(max_length=255, choices=STATES, default=EN_PREPARACION)
    num_max_players = models.IntegerField(default=0)
    num_players = models.IntegerField(default=0)


class Equipo(models.Model):
    # Relations
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, blank=True, null=True)
    # Fields
    name = models.CharField(max_length=255)
    max_num_players = models.IntegerField(default=0)
    num_players = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class EstadisticasJugador(models.Model):
    # Player Stats
    position1 = models.CharField(max_length=255)
    position2 = models.CharField(max_length=255)
    height = models.FloatField()

    # Player in Game Stats
    saque = models.IntegerField(default=0)
    recepcion = models.IntegerField(default=0)
    dedos = models.IntegerField(default=0)
    dedos_doble = models.IntegerField(default=0)
    ataque = models.IntegerField(default=0)
    foto = models.ImageField(default='static/assets/fondo.jpg', upload_to='images/')

    objects = models.Manager()


class Jugador(models.Model):
    def __str__(self) -> str:
        return "Jugador"

    # Relations 
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=True, null=True)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, blank=True, null=True)
    estadisticas_jugador = models.OneToOneField(
        EstadisticasJugador,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True,
    )

    # Fields
    name = models.CharField(max_length=255)
    rut = models.CharField(max_length=255)
    
    max_num_players = models.IntegerField(default=1)
    num_players = models.IntegerField(default=1)
    genero = models.CharField(max_length=255)

    objects = models.Manager()



class User(AbstractUser):
    ADMIN = 1
    NORMAL = 2
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (NORMAL, 'Normal'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    jugador = models.ForeignKey(Jugador,blank=True,null=True, on_delete=models.CASCADE)