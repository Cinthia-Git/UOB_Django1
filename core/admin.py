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


class CamposParametroAdmin(admin.ModelAdmin):
    list_display = [x.name for x in CamposParametro._meta.fields if x.name != 'localizacion']
admin.site.register(CamposParametro, CamposParametroAdmin)

#class LimitesAdmin(admin.ModelAdmin):
 #   list_display = [x.name for x in Limites._meta.fields if x.name != 'localizacion']
#admin.site.register(Limites, LimitesAdmin)



class VisorAdmin(LeafletGeoAdmin):
    list_display = [x.name for x in Visor._meta.fields if x.name != 'localizacion']
admin.site.register(Visor, VisorAdmin)
