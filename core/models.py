from django.db.models import *
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

paises=[
    (2,"Bolivia"), (3,"Peru")
]

monitoreos=[
    (4,"Calidad de agua"), (5,"Biomasa")
]

epocas=[
    (0,"seca"), (1,"humeda")
]

# Create your models here.


class Ubicacion(Model):
    pais=IntegerField(choices=paises)
    monitoreo=IntegerField(choices=monitoreos)
    point=models.PointField()
    
    #@property
    def lat_lng(self):
        return list(getattr(self.point, 'coords', []) [::-1])
    
    class Meta:
        verbose_name="Ubicación"
        verbose_name_plural="Ubicación"


class DatosGenerales(Model):
    id_datos_generales=IntegerField(primary_key=True)
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


class Limites(Model):
    simbolo=ForeignKey(Parametros,on_delete=CASCADE)
    CLASE_A=FloatField(
        validators = [MinValueValidator(3), MaxValueValidator(6)])
    #CLASE_B=FloatField
    #CLASE_C=FloatField
    #CLASE_D=FloatField
    #CLASE_E=FloatField

    def __str__(self):
        return self.simbolo
        
    class Meta:
        verbose_name="Límites"
        verbose_name_plural="Límites"

