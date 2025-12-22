from django import forms
from .models import Task
from .models import DatosPersonales
from .models import ExperienciaLaboral
from .models import Reconocimiento
from .models import CursoRealizado
from .models import ProductoAcademico
from .models import ProductoLaboral
""" from .models import VentaGarage """


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control',
                                           'placeholder':'write a title'}),
            'description':forms.Textarea(attrs={'class':'form-control',
                                           'placeholder':'write a description'}),                               
            'important':forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }

class datos_personalesform(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        exclude = ['usuario']

        labels = {
            'descripcion': '',
            'foto': '',
            'nombres': '',
            'apellidos': '',
            'nacionalidad': '',
            'lugar_nacimiento': '',
            'fecha_nacimiento': '',
            'numero_cedula': '',
            'sexo': '',
            'estado_civil': '',
            'licencia_conducir': '',
            'telefono_convencional': '',
            'telefono_fijo': '',
            'direccion_trabajo': '',
            'direccion_domiciliaria': '',
            'sitio_web': '',
        }

        widgets = {
            'descripcion':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Descripcion'
            }),
            'foto':forms.ClearableFileInput(attrs={
                'class':'form-control',
                'placeholder':'Ingrese una imagen'}),
              
            'nombres':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nombres'}),

            'apellidos':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Apellidos'}),

            'nacionalidad':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nacionalidad'}),

            'lugar_nacimiento':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Lugar de nacimiento'}),

            'fecha_nacimiento':forms.DateInput(attrs={
                'class':'form-control',
                'type':'date',
                'placeholder': 'DD-MM-YYYY'}),

            'numero_cedula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de cédula'}),

            'sexo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sexo'}),

            'estado_civil': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Estado_civil'}),

            'licencia_conducir': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Licencia_conducir'}),

            'telefono_convencional': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono convencional'}),

            'telefono_fijo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono fijo'}),

            'direccion_trabajo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección de trabajo'}),

            'direccion_domiciliaria': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección domiciliaria'}),

            'sitio_web':forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder':'Sitio web'}),
        }

class experiencia_laboralform(forms.ModelForm):
    class Meta:
        model =ExperienciaLaboral
        exclude = ['usuario']

        labels = {
            'nombres_empresa_trabajadas': 'Empresa',
            'cargos_de_trabajo': 'Cargo Ocupado',
            'lugar_empresa_trabajada': 'Ubicación',
            'fecha_inicio_gestion': 'Fecha de Inicio',
            'fecha_fin_gestion': 'Fecha de Finalización',
            'descripcion_funciones': 'Funciones y Logros',
        }

        widgets= {

            'nombres_empresa_trabajadas': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Nombre de la empresa'}),
            
            'cargos_de_trabajo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Cargo de trabajo'}),
            'lugar_empresa_trabajada': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Lugar de trabajo'}),

            'email_de_empresa': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email de la empresa'}),
            
            'sitio_web_empresa': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sitio web de la empresa'}),
            
            'nombre_contacto_empresarial': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de contacto de la empresa'}),
            
            'telefono_contacto_empresarial': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefono de contacto empresarial'}),

            'fecha_inicio_gestion': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fecha de inicio de gestion',
                'type': 'date'}),
            
            'fecha_fin_gestion': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fecha de fin de gestion',
                'type': 'date'}),

            'descripcion_funciones':forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripcion de fucion de la empresa'}),
        }

class ReconocimientoForm(forms.ModelForm):
    class Meta:
        model = Reconocimiento
        exclude = ['usuario']

        labels = {
            'tipo_reconocimiento': '',
            'fecha_reconocimiento': '',
            'descripcion_reconocimiento': '',
            'entidad_patrocinada': '',
            'nombre_contacto_auspicia': '',
            'telefonocontactoauspicia': '',
        }

        widgets = {
            'tipo_reconocimiento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Reconocimiento de area de:'}),
            
            'fecha_reconocimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Fecha del reconocimiento'}),
            
            'descripcion_reconocimiento': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descricion del reconocimiento'}),
            
            'entidad_patrocinada': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Institución o empresa'}),
            
            'nombre_contacto_auspicia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la persona de referencia'}),
            
            'telefonocontactoauspicia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de telefono'}),
        }

class CursoRealizadoForm(forms.ModelForm):
    class Meta:
        model = CursoRealizado
        exclude = ['usuario']

        labels = {
            'nombre_curso': '',
            'fecha_inicio': '',
            'fecha_fin': '',
            'total_horas': '',
            'descripcion': '',
            'entidad_patrocinadora': '',
            'nombre_contacto_auspicia': '',
            'telefono_contacto_auspicia': '',
            'email_empresa_patrocinadora': '',
            'mostrar_en_front': '¿Mostrar en perfil público?', # Es recomendable dejar este label por el checkbox
            'ruta_certificado': '',
        }

        widgets = {
            'nombre_curso': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: Curso de enseñanza sobre python'}),
            
            'fecha_inicio': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date',
                'placeholder': 'Inicio del curso'}),
            
            'fecha_fin': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date',
                'placeholder': 'Fin del curso'}),
            
            'total_horas': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: 114 horas'}),
            
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Descripcion del curso'}),
            
            'entidad_patrocinadora': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: Universidad xxx'}),
            
            'nombre_contacto_auspicia': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre del tutor o encargado del curso'}),
            
            'telefono_contacto_auspicia': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Numero de celular'}),
            
            'email_empresa_patrocinadora': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'xxxxx@xxx.com'}),
            
            'mostrar_en_front': forms.CheckboxInput(attrs={
                'class': 'form-check-input'}),
            
            'ruta_certificado': forms.FileInput(attrs={
                'class': 'form-control'}),
        }

class ProductoAcademicoForm(forms.ModelForm):
    class Meta:
        model = ProductoAcademico
        exclude = ['usuario']

        labels = {
            'nombre_recurso': '',
            'fecha_producto': '',
            'descripcion': '',
            'mostrar_en_front': '¿Público en perfil?',
        }

        widgets = {
            'nombre_recurso': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: Nombre trabajo de proyectos'}),
            
            'fecha_producto': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date',
                'placeholder': 'Fecha del producto'}),
            
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Indique una descripción corta'}),

            'proyectoacademico': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'link del proyecto'}),
            
            'mostrar_en_front': forms.CheckboxInput(attrs={
                'class': 'form-check-input'}),
        }

class ProductoLaboralForm(forms.ModelForm):
    class Meta:
        model = ProductoLaboral
        exclude = ['usuario']

        labels = {
            'nombre_producto': '',
            'fecha_producto': '',
            'descripcion': '',
            'mostrar_en_front': '¿Público en perfil?',
        }
        
        widgets = {
            'nombre_producto': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: Manual de Procedimientos, Software de Inventario'}),
            
            'fecha_producto': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date',
                'placeholder': 'Fecha del producto'}),
            
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Breve explicación del aporte laboral'}),

            'proyectolaboral': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'link del proyecto'}),
            
            'mostrar_en_front': forms.CheckboxInput(attrs={
                'class': 'form-check-input'}),
        }

""" class VentaGarageForm(forms.ModelForm):
    class Meta:
        model = VentaGarage
        exclude = ['usuario']

        widgets = {
            'nombre_producto': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nose'}),
            
            'estado_producto': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: Nuevo, Como nuevo, Usado'}),
            
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Breve reseña del estado o características'}),
            
            'valor_del_bien': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.01', # Permite decimales para centavos
                'placeholder': '0.00'}),
            
            'mostrar_en_front': forms.CheckboxInput(attrs={
                'class': 'form-check-input'}),
        } """