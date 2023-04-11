from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room,Topic
from .forms import RoomForm

#from django.http import HttpResponse
# Create your views here.

# Aqui se hace una instancia de los "templates\base", por cada ".html" se crea una funcion

# rooms = [
#     {'id': 1, 'name': 'Aprendo python'},
#     {'id': 2, 'name': 'Aprendo Django'},
#     {'id': 3, 'name': 'Aprendo Flask'}
# ]

def home(requst):

    q = requst.GET.get('q') if requst.GET.get('q') != None else ''
    ## filtrado para el sistema de busqueda
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms':rooms, 'topics': topics, 'room_count':room_count}
    return render(requst, "base/home.html",context )

def room(requst, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i

    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(requst, "base/room.html",context)

## Implementacion CRUD

# Se ha implementado la funcion createRoom -> se encarga de crear los Room

def createRoom(requst):
    form = RoomForm()
    if requst.method == 'POST':
        form = RoomForm(requst.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(requst, "base/room_form.html",context )

# Se ha implementado la funcion updateRoom -> se encarga de actualizar los Room

def updateRoom(requst, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)


    if requst.method == 'POST':
        form = RoomForm(requst.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = { 'form': form}
    return render(requst, 'base/room_form.html', context)

## Se va crear una funcion para eliminar las tablas creadas 

def deleteRoom(requst, pk):
    room = Room.objects.get(id=pk)
    if requst.method == 'POST':
        room.delete()
        return redirect('home')
    return render(requst, 'base/delete.html', {'obj': room})