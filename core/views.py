from django.shortcuts import render

from django.views.generic import TemplateView

from django.views.generic import ListView
from .models import DatosGenerales
from .models import Parametros
from .models import CamposParametro
#from .models import Limites
from .models import Visor



class Inicio(TemplateView):
    template_name = "core/index.html"


#class DatosGeneralesList(ListView) :
    #queryset = DatosGenerales.objects.filter(point_isnull-False )


# Create your views here.
