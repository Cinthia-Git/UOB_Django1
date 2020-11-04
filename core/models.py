from django.db.models import *
from django.contrib.gis.db import models


paises=[
    (0,"Bolivia"), (1,"Perú")
]

monitoreos=[
    (0,"Biomasa"), (1,"Calidad de agua")
]

epocas=[
    (0,"estiaje (seca)"), (1,"avenida (humeda)")
]

# Create your models here.



class DatosGenerales(Model):
    id_datos_generales=IntegerField(primary_key=True)
    pais=IntegerField(choices=paises)
    monitoreo=IntegerField(choices=monitoreos)
    epoca=IntegerField(choices=epocas)
    anyo=IntegerField()
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
    #id_parametro=IntegerField(primary_key=True)
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



class CamposParametro(Model):
    #id_parametro=IntegerField(primary_key=True)
    #ide_categoria=ForeignKey(Parametros,on_delete=CASCADE)
    CE=FloatField(max_length=50)
    Ods=FloatField(max_length=50)
    pH=FloatField(max_length=50)
    SDT=FloatField(max_length=50)
    SSed=FloatField(max_length=50)
    SST=FloatField(max_length=50)
    T=FloatField(max_length=50)
    Turb=FloatField(max_length=50)
    OD=FloatField(max_length=50)
    TDS=FloatField(max_length=50)
    Al=FloatField(max_length=50)
    As=FloatField(max_length=50)
    B=FloatField(max_length=50)
    Ca=FloatField(max_length=50)
    Cd=FloatField(max_length=50)
    Cu=FloatField(max_length=50)
    CrIII=FloatField(max_length=50)
    Fe=FloatField(max_length=50)
    Mn=FloatField(max_length=50)
    Hg=FloatField(max_length=50)
    Ni=FloatField(max_length=50)
    Pb=FloatField(max_length=50)
    Se=FloatField(max_length=50)
    Na=FloatField(max_length=50)
    Zn=FloatField(max_length=50)
    NH3=FloatField(max_length=50)
    Cl=FloatField(max_length=50)
    P=FloatField(max_length=50)
    PO43=FloatField(max_length=50)
    N_T=FloatField(max_length=50)
    SO42=FloatField(max_length=50)
    S2=FloatField(max_length=50)
    AyG=FloatField(max_length=50)
    COT=FloatField(max_length=50)
    C=FloatField(max_length=50)
    DBOs=FloatField(max_length=50)
    SAAM=FloatField(max_length=50)
    Colifecal=FloatField(max_length=50)
    Parasitos=FloatField(max_length=50)




    def __str__(self):
        return self.id_nombre

    class Meta:
        verbose_name="Campos Parámetro"
        verbose_name_plural="Campos Parámetro"





#class Limites(Model):
    #id_limite=IntegerField(primary_key=True)
    #nombre=ForeignKey(Parametros,on_delete=CASCADE)
    #claseA=FloatField(max_length=50)
    #claseB=FloatField(max_length=50)
    #claseC=FloatField(max_length=50)
    #claseD=FloatField(max_length=50)
    #clase_critica=FloatField(max_length=50)

    #def __str__(self):
     #   return self.nombre
        
    #class Meta:
     #   verbose_name="Límites"
      #  verbose_name_plural="Límites"


class Visor(Model):
    point=models.PointField()


    #@property
    def lat_lng(self):
        return list(getattr(self.point, 'coords', []) [::-1])
    
    class Meta:
        verbose_name="Visor"
        verbose_name_plural="Visor"

