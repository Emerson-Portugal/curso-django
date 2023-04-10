from django.contrib import admin

# Register your models here.

## una vez que ya hemos creado nuerstros modulos(tablas para la base de datos)
## Tenemos que agregarlos al panel de administracion


from .models import Room, Message, Topic

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)