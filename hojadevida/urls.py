"""
URL configuration for hojadevida project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from paginausuario import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    #aqui
    path('datos_personales/crear/', views.crear_datos_personales, name='crear_datos_personales'),
    path('curso/crear/', views.crear_CursoRealizado, name='crear_CursoRealizado'),
    path('curso/editar/<int:experiencia_id>/', views.crear_CursoRealizado, name='editar_CursoRealizado'),
    path('curso/eliminar/<int:pk>/', views.eliminar_cursorealizado, name='eliminar_CursoRealizado'),
    path('experiencia/crear/', views.crear_experiencia_laboral, name='crear_experiencia_laboral'),
    path('experiencia/editar/<int:experiencia_id>/', views.crear_experiencia_laboral, name='editar_experiencia_laboral'),
    path('experiencia/eliminar/<int:pk>/', views.eliminar_experiencia_laboral, name='eliminar_experiencia_laboral'),
    path('producto_laboral/crear/', views.crear_ProductoLaboral, name='crear_ProductoLaboral'),
    path('producto_laboral/editar/<int:experiencia_id>/', views.crear_ProductoLaboral, name='editar_ProductoLaboral'),
    path('producto_laboral/eliminar/<int:pk>/', views.eliminar_producto_laboral, name='eliminar_producto_laboral'),
    path('producto_academico/crear/', views.crear_ProductoAcademico, name='crear_ProductoAcademico'),
    path('producto_academico/editar/<int:experiencia_id>/', views.crear_ProductoAcademico, name='editar_ProductoAcademico'),
    path('producto_academico/eliminar/<int:pk>/', views.eliminar_producto_academico, name='eliminar_producto_academico'),
    path('reconocimiento/crear/', views.crear_reconocimiento, name='crear_reconocimiento'),
    path('reconocimiento/editar/<int:experiencia_id>/', views.crear_reconocimiento, name='editar_reconocimiento'),
    path('reconocimietno/eliminar/<int:pk>/', views.eliminar_reconocimiento, name='eliminar_reconocimiento'),
    path('hoja_de_vida/',views.hoja_de_vida, name='hoja_de_vida'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('hoja-de-vida/',views.u_hoja_de_vida, name='u_hoja_de_vida'),
    path('hoja-de-vida/<str:invitado>/', views.u_hoja_de_vida, name='u_hoja_de_vida_user'),
    path('DatosPersonales',views.DatosPersonales, name='DatosPersonales'),
    

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

