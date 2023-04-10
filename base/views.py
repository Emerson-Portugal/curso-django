from django.shortcuts import render
from .models import Room
#from django.http import HttpResponse
# Create your views here.

# Aqui se hace una instancia de los "templates\base", por cada ".html" se crea una funcion

# rooms = [
#     {'id': 1, 'name': 'Aprendo python'},
#     {'id': 2, 'name': 'Aprendo Django'},
#     {'id': 3, 'name': 'Aprendo Flask'}
# ]

def home(requst):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(requst, "base/home.html",context )

def room(requst, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i

    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(requst, "base/room.html",context)