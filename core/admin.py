from django.contrib import admin
from core.models import *
from leaflet.admin import LeafletGeoAdmin
from .models import DatosGenerales
from .models import Parametros
from .models import Lugar

# Register your models here.
#admin.site.register(DatosGenerales)
#admin.site.register(Parametros)
#admin.site.register(Lugar, LeafletGeoAdmin)


class DatosGeneralesAdmin(LeafletGeoAdmin):
    list_display = ('DatosGenerales', 'location')

admin.site.register(DatosGenerales, DatosGeneralesAdmin)


class ParametrosAdmin(LeafletGeoAdmin):
    list_display = ('Parametros', 'location')

admin.site.register(Parametros, ParametrosAdmin)



class LugarAdmin(LeafletGeoAdmin):
    list_display = ('Lugar', 'location')
    list_filter = ('Lugar', 'location')

admin.site.register(Lugar, LugarAdmin)