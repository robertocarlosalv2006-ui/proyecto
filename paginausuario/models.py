from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Task(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True,blank=True)
    important=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title +'- by'+ self.user.username
    

class DatosPersonales(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    descripcion=models.TextField(max_length=1000, blank=True)
    foto = models.ImageField(upload_to='perfil/', null=True, blank=True)
    nombres = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    nacionalidad = models.CharField(max_length=100, blank=True)
    lugar_nacimiento = models.CharField(max_length=100, blank=True)

    fecha_nacimiento = models.DateField(blank=True, null=True)
    numero_cedula = models.CharField(max_length=20, blank=True)

    sexo = models.CharField(max_length=20, blank=True)
    estado_civil = models.CharField(max_length=20, blank=True)
    licencia_conducir = models.CharField(max_length=50, blank=True)

    telefono_convencional = models.CharField(max_length=20, blank=True)
    telefono_fijo = models.CharField(max_length=20, blank=True)

    direccion_trabajo = models.CharField(max_length=150, blank=True)
    direccion_domiciliaria = models.CharField(max_length=150, blank=True)

    sitio_web = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class ExperienciaLaboral(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='experiencias'
    )

    nombres_empresa_trabajadas = models.CharField(max_length=100, blank=True)
    cargos_de_trabajo=models.CharField(max_length=100, blank=True)
    lugar_empresa_trabajada = models.CharField(max_length=100, blank=True)
    email_de_empresa = models.CharField(max_length=100, blank=True)
    sitio_web_empresa = models.URLField(blank=True)
    nombre_contacto_empresarial= models.CharField(max_length=100, blank=True)
    telefono_contacto_empresarial= models.CharField(max_length=100, blank=True)
    fecha_inicio_gestion= models.DateField(blank=True, null=True)
    fecha_fin_gestion= models.DateField(blank=True, null=True)
    descripcion_funciones= models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.cargos_de_trabajo} en {self.nombres_empresa_trabajadas}"

    class Meta:
        verbose_name = "Experiencia Laboral"
        verbose_name_plural = "Experiencias Laborales"
        ordering = ['-fecha_inicio_gestion']


class Reconocimiento(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='reconocimiento'
    )

    tipo_reconocimiento = models.CharField(max_length=100, blank=True)
    fecha_reconocimiento = models.DateField(null=True, blank=True)
    descripcion_reconocimiento = models.TextField(max_length=1000,blank=True)
    entidad_patrocinada = models.CharField(max_length=100, blank=True)
    nombre_contacto_auspicia = models.CharField(max_length=100, blank=True)
    telefonocontactoauspicia = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.tipo_reconocimiento} - {self.usuario.username}"
    

class CursoRealizado(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='cursos_realizados'
    )

    nombre_curso = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    total_horas = models.IntegerField(null=True, blank=True)
    descripcion = models.CharField(max_length=100, blank=True)
    entidad_patrocinadora = models.CharField(max_length=100, blank=True)
    nombre_contacto_auspicia = models.CharField(max_length=100, blank=True)
    telefono_contacto_auspicia = models.CharField(max_length=60, blank=True)
    email_empresa_patrocinadora = models.EmailField(max_length=60, blank=True)
    mostrar_en_front = models.BooleanField(default=True) # Equivale al 'bit'
    ruta_certificado = models.FileField(upload_to='certificados/', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_curso
    

class ProductoAcademico(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='productos_academicos'
    )
    nombre_recurso = models.CharField(max_length=100)
    fecha_producto = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=100, blank=True)
    mostrar_en_front = models.BooleanField(default=True)
    proyectoacademico = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nombre_recurso} ({self.clasificador})"
    
class ProductoLaboral(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='productos_laborales'
    )
    nombre_producto = models.CharField(max_length=100)
    fecha_producto = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=100, blank=True)
    mostrar_en_front = models.BooleanField(default=True)
    proyectolaboral = models.URLField(blank=True)

    def __str__(self):
        return self.nombre_producto
    
""" class VentaGarage(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='ventas_garage'
    )
    
    nombre_producto = models.CharField(max_length=100)
    estado_producto = models.CharField(max_length=40, blank=True)
    descripcion = models.CharField(max_length=100, blank=True)
    valor_del_bien = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    mostrar_en_front = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_producto} - ${self.valor_del_bien}"
     """
# Create your models here.
