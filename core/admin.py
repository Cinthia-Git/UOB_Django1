from django.contrib import admin
from core.models import *
from leaflet.admin import LeafletGeoAdmin

#from .models import DatosGenerales
#from .models import Parametros
#from .models import Lugar

# Register your models here.
#admin.site.register(DatosGenerales)
#admin.site.register(Parametros)
#admin.site.register(Lugar, LeafletGeoAdmin)


class DatosGeneralesAdmin(admin.ModelAdmin):
     list_display = [x.name for x in DatosGenerales._meta.fields if x.name != 'localizacion']
admin.site.register(DatosGenerales, DatosGeneralesAdmin)
#('DatosGenerales', 'location')

class ParametrosAdmin(admin.ModelAdmin):
     list_display = [x.name for x in Parametros._meta.fields if x.name != 'localizacion']
admin.site.register(Parametros, ParametrosAdmin)

class LugarAdmin(LeafletGeoAdmin):
    list_display = [x.name for x in Lugar._meta.fields if x.name != 'localizacion']
admin.site.register(Lugar, LugarAdmin)