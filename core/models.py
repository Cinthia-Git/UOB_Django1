from django.db.models import *
from django.contrib.gis.db import models

paises=[
    (0,"bolivia"), (1,"peru")
]


monitoreos=[
    (0,"calidad"), (1,"biomasa")
]


epocas=[
    (0,"seca"), (1,"humeda")
]
# Create your models here.
class DatosGenerales(Model):
    id_datos_generales=IntegerField(primary_key=True)
    pais=IntegerField(choices=paises)
    tipo_monitoreo=IntegerField(choices=monitoreos)
    anyo=IntegerField()
    epoca=IntegerField(choices=epocas)
    fecha=DateField()
    hora=TimeField()
    nombre=CharField(max_length=50)
    punto_muestreo=CharField(max_length=50)
    tipo=CharField(max_length=50)
    departamento=CharField(max_length=50)
    municipio=CharField(max_length=50)
    comunidad=CharField(max_length=50)
    latitud=FloatField()
    longitud=FloatField()
    zona_utm=CharField(max_length=10)
    altura=FloatField()
 
    def __str__(self):
        return self.nombre

    class Meta:
        ordering=("anyo",)
        verbose_name="dato general"
        verbose_name_plural="Datos Generales"



class Parametros(Model):
    id_datos_generales=ForeignKey(DatosGenerales,on_delete=CASCADE)
    categoria=CharField(max_length=50)
    nombre=CharField(max_length=50)
    simbolo=CharField(max_length=15)
    unidad_medida=CharField(max_length=10)


    def __str__(self):
        return self.categoria

    class Meta:
        ordering=("nombre",)
        verbose_name="Parámetro"
        verbose_name_plural="Parámetros"




class Lugar(Model):
    nom=CharField(max_length=100)
    point=models.PointField()
    
    #@property
    def lat_lng(self):
        return list(getattr(self.point, 'coords', []) [::-1])
    
    class Meta:
        verbose_name_plural ="Lugares"





#class Límites_RMCH(Model):
    #id_parametro= 
    #CLASE_A=FloatField
    #CLASE_B=
    #CLASE_C=
    #CLASE_D=
    #CLASE_E= 
