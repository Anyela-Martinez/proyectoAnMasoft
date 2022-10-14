from dataclasses import FrozenInstanceError
from django.db import models

from usuarios.models import Usuario

# Create your models here.
class Publicacion(models.Model):
    nombrePubli=models.CharField(max_length=60, verbose_name="Nombre de la Publicación")

    descripPublic=models.CharField(max_length=60, verbose_name="Descripción de la Publicación")

    linkPubli=models.CharField(max_length=60, verbose_name="Link de la Publicación")

    class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    Estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    class Jornada(models.Model):
        JM='MAÑANA', _('Jornada Mañana')
        JT='TARDE', _('Jornada Tarde')
    Jornada=models.CharField(max_length=2,choices=Jornada.choices, default=Jornada.JM, verbose_name="Jornada")

    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name='Usuario')

    docente=models.ForeignKey(Docente, on_delete=models.CASCADE,verbose_name='Docente')

    tipoPublicacion=models.ForeignKey(TipoPublicacion, on_delete=models.CASCADE,verbose_name='Tipo de Publicación')

    grado=models.ForeignKey(Grado, on_delete=models.CASCADE,verbose_name='Grado')

