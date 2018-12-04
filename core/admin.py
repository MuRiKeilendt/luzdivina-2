from django.contrib import admin
from .models import Comunidad, Boda, Bautizo, Comunion, Comunidadcatolica
# Register your models here.
admin.site.register(Comunidad)
admin.site.register(Boda)
admin.site.register(Bautizo)
admin.site.register(Comunion)
admin.site.register(Comunidadcatolica)

