from alumnos.models import Platillo

# Crear platillos (asegúrate de que los archivos de imagenes existen en la ruta especificada)
Platillo.objects.create(nombre="Comida 1", descripcion="Descripción de comida 1", precio=1000.00, imagen="img/comida1.jpg")
Platillo.objects.create(nombre="Comida 2", descripcion="Descripción de comida 2", precio=2000.00, imagen="img/comida2.webp")
Platillo.objects.create(nombre="Comida 3", descripcion="Descripción de comida 3", precio=3000.00, imagen="img/comida3.jpg")
Platillo.objects.create(nombre="Comida 4", descripcion="Descripción de comida 4", precio=4000.00, imagen="img/comida4.jpg")
