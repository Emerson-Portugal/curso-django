## Aqui se va a procesar los valores que se ingresen al formulario

from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # fields = '__all__' -> vamos agregar todo los valores de la clase -> 'class Room(models.Model):'
        fields = '__all__'