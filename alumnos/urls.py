# alumnos/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.vista_formulario, name='formulario'),
    path('exito/', views.index, name='exito'),
    path('base/', views.base, name='base'),
    path('registro/', views.vista_registro, name='registro'),
    path('admin/', views.vista_admin, name='admin'),
    path('login/', views.vista_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('contacto/', views.vista_contacto, name='contacto'),
    path('admin/ver/<int:solicitud_id>/', views.ver_solicitud, name='ver_solicitud'),
    path('admin/eliminar/<int:solicitud_id>/', views.eliminar_solicitud, name='eliminar_solicitud'),
    path('admin/responder/<int:solicitud_id>/', views.responder_solicitud, name='responder_solicitud'),
    path('admin_opciones/', views.admin_opciones, name='admin_opciones'),
    path('ofertas/', views.ofertas, name='ofertas'),#AUN NO LA AGREGO XD
    path('platos_especiales/', views.platos_especiales, name='platos_especiales'),
    path('carrito/', views.carrito, name='carrito'),
    path('admin/platillos/', views.admin_platillos, name='admin_platillos'),
    path('admin/platillos/agregar/', views.agregar_platillo, name='agregar_platillo'),
    path('admin/platillos/editar/<int:platillo_id>/', views.editar_platillo, name='editar_platillo'),
    path('admin/platillos/eliminar/<int:platillo_id>/', views.eliminar_platillo, name='eliminar_platillo'),
    path('admin/platillos/ver/<int:platillo_id>/', views.ver_platillo, name='ver_platillo'),
    path('pagar/', views.pagar, name='pagar'),
    path('catalogo/', views.catalogo, name='catalogo'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 