from django.db import models
from django.contrib.auth.models import User

# Create your models here.

## aqui vamos a crear las tablas para la base de datos de nuestra aplicacion

'''
host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) -> hace referncia al usuario registrado en la base de datos

topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) -> Hace referencia a Tema 



'''


## Temas


class Topic (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name





class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # Topic, on_delete=models.SET_NULL, null=True) -> para este caso no se va a eliminar la Tabla Room, solo se podra nulo si no se ingresa valores 

    name = models.CharField(max_length=200)

    #(null=True, blank=True) -> puede estar en blanco o no, este partado
    description = models.TextField(null=True, blank=True)
    # participants=
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    '''
    auto_now=True -> crea una instancia cada ves que modifica y se guarda

    auto_now_add=True -> Crea una instancia solo una ves creado
    '''         
    def __str__(self):
        return self.name
    
'''
Union de una tabla a la otra (un usuario puede tener varias publicaciones, pero muchas publicaciones pueden tener un solo usuario (uno a muchos) )
'''

## Mensaje
class Message(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #(Room, on_delete=models.CASCADE) -> Si no tiene ninguna clase padre, se elininara tambien la clase hijo (Message)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #models.TextField() -> Aqui es obligatorio llenar la informacion
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]