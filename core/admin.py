from django.contrib import admin
from core.models import *
from django.contrib.gis.admin import LeafletGeoAdmin
from .models import DatosGenerales
from .models import Parametros
from .models import Lugar

# Register your models here.
admin.site.register(DatosGenerales)
admin.site.register(Parametros)
admin.site.register(Lugar, LeafletGeoAdmin)

@admin.register (DatosGenerales)
class DatosGeneralesAdmin(LeafletGeoAdmin):
    list_display = ('DatosGenerales', 'location')
admin.site.register(DatosGenerales, DatosGeneralesAdmin)

@admin.register (Parametros)
class ParametrosAdmin(LeafletGeoAdmin):
    list_display = ('Parametros', 'location')
admin.site.register(Parametros, ParametrosAdmin)


