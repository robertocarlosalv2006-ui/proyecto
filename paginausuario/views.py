from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
#from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import DatosPersonales
from .models import ExperienciaLaboral
from .models import Reconocimiento
from .models import CursoRealizado
from .models import ProductoAcademico
from .models import ProductoLaboral
from .forms import datos_personalesform
from .forms import experiencia_laboralform
from .forms import ReconocimientoForm
from .forms import CursoRealizadoForm
from .forms import ProductoAcademicoForm
from .forms import ProductoLaboralForm
from django.contrib import messages

def u_hoja_de_vida(request):
    datos = DatosPersonales.objects.filter(usuario__username='Roberto').first()
    experiencia = ExperienciaLaboral.objects.filter(usuario__username='Roberto')
    reconocimiento = Reconocimiento.objects.filter(usuario__username='Roberto')
    curso = CursoRealizado.objects.filter(usuario__username='Roberto')
    producto_academico = ProductoAcademico.objects.filter(usuario__username='Roberto')
    producto_laboral = ProductoLaboral.objects.filter(usuario__username='Roberto')
    return render(request, 'u_hoja_de_vida.html', {'datos': datos, 'experiencia':experiencia, 'reconocimiento': reconocimiento, 'curso': curso, 'producto_academico': producto_academico, 'producto_laboral': producto_laboral,})
        

def hoja_de_vida(request):
    datos = DatosPersonales.objects.filter(usuario=request.user).first()
    experiencia=ExperienciaLaboral.objects.filter(usuario=request.user)
    reconocimiento=Reconocimiento.objects.filter(usuario=request.user)
    curso=CursoRealizado.objects.filter(usuario=request.user)
    producto_academico=ProductoAcademico.objects.filter(usuario=request.user)
    producto_laboral=ProductoLaboral.objects.filter(usuario=request.user)
    return render(request, 'hoja_de_vida.html',{
        'datos': datos,
        'experiencia': experiencia,
        'reconocimiento': reconocimiento,
        'curso': curso,
        'producto_academico': producto_academico,
        'producto_laboral': producto_laboral,
        })


@login_required
def crear_datos_personales(request):
    instancia = DatosPersonales.objects.filter(usuario=request.user).first()
    if request.method == 'POST':
        form = datos_personalesform(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            datos=form.save(commit=False)
            datos.usuario= request.user
            datos.save()
            messages.success(request, "Datos guardados correctamente.")
            return redirect('hoja_de_vida')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
            print(form.errors)
    else:
        form = datos_personalesform(instance=instancia)
        

    return render(request, 'crear_datos_personales.html', {
        'form': form,
        'editando': instancia is not None
    })

@login_required
def crear_experiencia_laboral(request, experiencia_id=None):
    instancia = None
    if experiencia_id:
        instancia = ExperienciaLaboral.objects.filter(id=experiencia_id, usuario=request.user).first()

    if request.method == 'POST':
        form = experiencia_laboralform(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            datos=form.save(commit=False)
            datos.usuario= request.user
            datos.save()
            messages.success(request, "Datos guardados correctamente.")
            return redirect('hoja_de_vida')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
            print(form.errors)
    else:
        form = experiencia_laboralform(instance=instancia)
        

    return render(request, 'crear_experiencia_laboral.html', {
        'form': form,
        'editando': instancia is not None
    })

def eliminar_experiencia_laboral(request, pk):
    # Buscamos la experiencia por su ID (pk)
    experiencia = get_object_or_404(ExperienciaLaboral, id=pk)
    
    if request.method == 'POST':
        experiencia.delete()
        messages.success(request, "La experiencia laboral ha sido eliminada correctamente.")
        return redirect('hoja_de_vida') # Redirige a tu vista principal
    
    # Si alguien intenta entrar por URL (GET), lo mandamos de vuelta
    return redirect('hoja_de_vida')


@login_required
def crear_reconocimiento(request, experiencia_id=None):
    instancia = None
    if experiencia_id:
        instancia = Reconocimiento.objects.filter(id=experiencia_id, usuario=request.user).first()

    if request.method == 'POST':
        form = ReconocimientoForm(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            datos=form.save(commit=False)
            datos.usuario= request.user
            datos.save()
            messages.success(request, "Datos guardados correctamente.")
            return redirect('hoja_de_vida')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
            print(form.errors)
    else:
        form = ReconocimientoForm(instance=instancia)
        

    return render(request, 'crear_reconocimiento.html', {
        'form': form,
        'editando': instancia is not None
    })

def eliminar_reconocimiento(request, pk):
    # Buscamos la experiencia por su ID (pk)
    reconocimiento = get_object_or_404(Reconocimiento, id=pk)
    
    if request.method == 'POST':
        reconocimiento.delete()
        messages.success(request, "El reconocimiento ha sido eliminada correctamente.")
        return redirect('hoja_de_vida') # Redirige a tu vista principal
    
    # Si alguien intenta entrar por URL (GET), lo mandamos de vuelta
    return redirect('hoja_de_vida')

@login_required
def crear_CursoRealizado(request, experiencia_id=None):
    instancia = None
    if experiencia_id:
        instancia = CursoRealizado.objects.filter(id=experiencia_id, usuario=request.user).first()

    if request.method == 'POST':
        form = CursoRealizadoForm(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            datos=form.save(commit=False)
            datos.usuario= request.user
            datos.save()
            messages.success(request, "Datos guardados correctamente.")
            return redirect('hoja_de_vida')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
            print(form.errors)
    else:
        form = CursoRealizadoForm(instance=instancia)
        

    return render(request, 'crear_CursoRealizado.html', {
        'form': form,
        'editando': instancia is not None
    })

def eliminar_cursorealizado(request, pk):
    # Buscamos la experiencia por su ID (pk)
    curso = get_object_or_404(CursoRealizado, id=pk)
    
    if request.method == 'POST':
        curso.delete()
        messages.success(request, "El curso ha sido eliminada correctamente.")
        return redirect('hoja_de_vida') # Redirige a tu vista principal
    
    # Si alguien intenta entrar por URL (GET), lo mandamos de vuelta
    return redirect('hoja_de_vida')

@login_required
def crear_ProductoAcademico(request, experiencia_id=None):
    instancia = None
    if experiencia_id:
        instancia = ProductoAcademico.objects.filter(id=experiencia_id, usuario=request.user).first()

    if request.method == 'POST':
        form = ProductoAcademicoForm(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            datos=form.save(commit=False)
            datos.usuario= request.user
            datos.save()
            messages.success(request, "Datos guardados correctamente.")
            return redirect('hoja_de_vida')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
            print(form.errors)
    else:
        form = ProductoAcademicoForm(instance=instancia)

    return render(request, 'crear_ProductoAcademico.html', {
        'form': form,
        'editando': instancia is not None
    })

def eliminar_producto_academico(request, pk):
    # Buscamos la experiencia por su ID (pk)
    producto_academico = get_object_or_404(ProductoAcademico, id=pk)
    
    if request.method == 'POST':
        producto_academico.delete()
        messages.success(request, "El producto academico ha sido eliminada correctamente.")
        return redirect('hoja_de_vida') # Redirige a tu vista principal
    
    # Si alguien intenta entrar por URL (GET), lo mandamos de vuelta
    return redirect('hoja_de_vida')


@login_required
def crear_ProductoLaboral(request, experiencia_id=None):
    instancia = None
    if experiencia_id:
        instancia = ProductoLaboral.objects.filter(id=experiencia_id, usuario=request.user).first()

    if request.method == 'POST':
        form = ProductoLaboralForm(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            datos=form.save(commit=False)
            datos.usuario= request.user
            datos.save()
            messages.success(request, "Datos guardados correctamente.")
            return redirect('hoja_de_vida')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
            print(form.errors)
    else:
        form = ProductoLaboralForm(instance=instancia)
        

    return render(request, 'crear_ProductoLaboral.html', {
        'form': form,
        'editando': instancia is not None
    })

def eliminar_producto_laboral(request, pk):
    # Buscamos la experiencia por su ID (pk)
    producto_laboral = get_object_or_404(ProductoLaboral, id=pk)
    
    if request.method == 'POST':
        producto_laboral.delete()
        messages.success(request, "El producto laboral ha sido eliminada correctamente.")
        return redirect('hoja_de_vida') # Redirige a tu vista principal
    
    # Si alguien intenta entrar por URL (GET), lo mandamos de vuelta
    return redirect('hoja_de_vida')

def home(request):
    return render(request, 'home.html')
   
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'Roberto' and password == 'adminroberto':
            user, created = User.objects.get_or_create(username='Roberto')
            if created:
                user.set_password('adminroberto') # Le asignamos la clave la primera vez
                user.save()
            login(request, user)
            return redirect('hoja_de_vida')


def signout(request):
    logout(request)
    return redirect('home')


def signup(request):
    if request.method =='GET':
        return render(request,'signup.html',
            {'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tasks')
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {"form":UserCreationForm, "error":"Username already exists"},
                )
        return render(
            request,
                "signup.html",
                {"form":UserCreationForm, "error":"Password do not match"},
         )
        

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request,'tasks.html',{'tasks':tasks,'tipopagina':'Hoja de vida'})

@login_required
def tasks_completed(request):
    tasks=Task.objects.filter(user=request.user,datecompleted__isnull=False).order_by('-datecompleted')
    return render(request,'tasks.html',{'tasks':tasks,'tipopagina':'Tareas Completadas'})

@login_required
def task_detail(request, task_id):
   if request.method == 'GET':
        task = get_object_or_404(Task,pk=task_id,user=request.user)
        form = TaskForm(instance=task)
        return render(request,'task_detail.html',{
            'task':task,
            'form':form
            })
   else:
       try:
            task = get_object_or_404(Task,pk=task_id,user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
       except ValueError:
            return render(request,'task_detail.html',{
            'task':task,
            'form':form,
            'error':'Error updating tasks'
            })