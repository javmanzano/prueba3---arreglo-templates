from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormularioLogin, FormularioRegistro,FormularioAutenticacionPersonalizado
from django.contrib.auth.decorators import user_passes_test 
from .models import SolicitudContacto, Platillo , Carrito
from django.contrib.auth.models import User
from .forms import FormularioContacto  , RespuestaContactoForm  , PlatilloForm
from collections import defaultdict
from django.shortcuts import redirect
from django.contrib import messages




def index(request):
    return render(request, 'index.html')

def es_admin(user):
    return user.is_superuser #practicamente un boolean

@user_passes_test(es_admin) #Restringje el acceso a todos los user, menos el admin, se usa la funcion de arriba para verificar si es superuser
def vista_admin(request):
    return render(request, 'admin/admin_opciones.html')

@user_passes_test(es_admin)
def admin_opciones(request):
    solicitudes = SolicitudContacto.objects.all() #mediante el modelo SolicitudContacto devuelve los objetos para ver las solicitudes en el crud
    return render(request, 'admin/admin_contacto.html', {'solicitudes': solicitudes})



@user_passes_test(es_admin)
def ver_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudContacto, pk=solicitud_id) #si falla en obtener pk primary key devolvera error 404 
    return render(request, 'admin/ver_solicitud.html', {'solicitud': solicitud})

@user_passes_test(es_admin)
def eliminar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudContacto, pk=solicitud_id) #si falla en obtener pk primary key devolvera error 404 
    solicitud.delete()
    return redirect('admin_opciones')

@user_passes_test(es_admin)
def responder_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudContacto, pk=solicitud_id) #si falla en obtener pk primary key devolvera error 404 
    if request.method == 'POST':
        form = RespuestaContactoForm(request.POST) #extrae RespuestaContactoForm desde forms
        if form.is_valid():
            # Procesar el formulario si es necesario, pero no enviar correo
            response = form.cleaned_data['response'] #lo mismo de antes, para usar los datos verifica que fueran validos,
            # Aquí podrías guardar la respuesta en la base de datos si es necesario
        return redirect('admin_opciones')  # Redirigir al nombre de la vista
    else:
        form = RespuestaContactoForm()
    return render(request, 'admin/responder_solicitud.html', {'form': form, 'solicitud': solicitud}) 

@user_passes_test(es_admin)
def admin_platillos(request):
    platillos = Platillo.objects.all()
    return render(request, 'admin/admin_platillos.html', {'platillos': platillos})

@user_passes_test(es_admin)
def ver_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, pk=platillo_id)
    return render(request, 'admin/ver_platillo.html', {'platillo': platillo})


@user_passes_test(es_admin)
def agregar_platillo(request):
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_platillos')
    else:
        form = PlatilloForm()
    return render(request, 'admin/agregar_platillo.html', {'form': form})


@user_passes_test(es_admin)
def editar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES, instance=platillo)
        if form.is_valid():
            if 'imagen' not in request.FILES and 'imagen' in form.cleaned_data:
                form.cleaned_data['imagen'] = platillo.imagen
            form.save()
            return redirect('admin_platillos')
    else:
        form = PlatilloForm(instance=platillo)
    return render(request, 'admin/editar_platillo.html', {'form': form})


@user_passes_test(es_admin)
def eliminar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, pk=platillo_id)
    if request.method == 'POST':
        platillo.delete()
        return redirect('admin_platillos')
    return render(request, 'admin/eliminar_platillo.html', {'platillo': platillo})



def vista_formulario(request):
    if request.method == 'POST':
        form = HOLA(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = HOLA()
    return render(request, 'formulario.html', {'form': form})


def base(request):
    return render(request, 'base.html')
    
def vista_registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.username = form.cleaned_data['email']  
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            messages.success(request, 'Tu cuenta ha sido creada exitosamente.')
            return redirect('login')  
        else:
            messages.error(request, 'Correo ya registrado.')
    else:
        form = FormularioRegistro()
    return render(request, 'registro.html', {'form': form})


def vista_login(request):
    if request.method == 'POST':
        form = FormularioLogin(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin')
                else:
                    return redirect('index')
    else:
        form = FormularioLogin()
    return render(request, 'login.html', {'form': form})

def vista_contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormularioContacto()
    return render(request, 'contacto.html', {'form': form})


def vista_inicio_sesion_personalizada(request):
    if request.method == 'POST':
        form = FormularioAutenticacionPersonalizado(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirige a la página que prefieras
    else:
        form = FormularioAutenticacionPersonalizado(request)

    return render(request, 'login.html', {'form': form})




@user_passes_test(es_admin)
def ofertas(request):
    # Lógica para mostrar las ofertas
    return render(request, 'ofertas.html') #AUN NO LAS AGREGO JSJSJS


def platos_especiales(request):
    platillos = Platillo.objects.all()
    return render(request, 'platos_especiales.html', {'platillos': platillos})


@login_required
def carrito(request):
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            item_id = request.POST.get('item_id')
            item = get_object_or_404(Carrito, id=item_id, usuario=request.user)
            item.delete()
        else:
            platillo_id = request.POST.get('platillo_id')
            platillo = get_object_or_404(Platillo, id=platillo_id)
            cantidad = int(request.POST.get('cantidad', 1))
            carrito_items = Carrito.objects.filter(platillo=platillo, usuario=request.user)
            if carrito_items.exists():
                carrito_item = carrito_items.first()
                carrito_item.cantidad += cantidad
                carrito_item.save()
            else:
                Carrito.objects.create(platillo=platillo, cantidad=cantidad, usuario=request.user)

    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = 0
    for item in carrito_items:
        item.subtotal = item.platillo.precio * item.cantidad
        total += item.subtotal
    
    return render(request, 'carrito.html', {'carrito_items': carrito_items, 'total': total})

@login_required
def pagar(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.platillo.precio * item.cantidad for item in carrito_items)
    return render(request, 'pagar.html', {'carrito_items': carrito_items, 'total': total})


def redireccionar(request):
    return redirect('/alumnos/')