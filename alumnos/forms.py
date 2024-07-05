from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import SolicitudContacto , Platillo
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import authenticate

# CLASE PARA CREACION DEL FORMULARIO
class FormularioRegistro(forms.ModelForm): #
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput(), label="Confirmar contraseña") #se agrega el campo de confirmar contrasena

    class Meta: #clase meta nos trae model,fields,widgets labels 
        model = User #USER predeterminado de django se importa
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'password': 'Contraseña',
        }
    
    def clean_email(self): #VERIFICA QUE EL CORREO NO EXISTA 
        email = self.cleaned_data.get('email') # si los datos que ingreso son validos recupera el email 'dudas' cleande data etc viene del diccionario de django
        if User.objects.filter(email=email).exists(): # busca el correo de los usuarios registrados, buscando un email que sea igual al ingresado , Si la consulta resulta true tira la alerta de abajo
            raise forms.ValidationError("Este correo ya está registrado.") #verifica el objeto email en la base de datos para la comparacion, 
        return email

    def clean(self): # VERIFICA QUE LA CONTRASENA Y CONFIRMAR CONTRASENA SEAN IGUALES
        cleaned_data = super().clean() #antes de verificar se asegura que los datos son validos
        contraseña = cleaned_data.get("password") #obtiene contrasena de los datos ya filtrados
        confirmar_contraseña = cleaned_data.get("confirmar_contraseña") #obtiene contrasena de los datos ya filtrados

        if contraseña != confirmar_contraseña:
            self.add_error('confirmar_contraseña', "Las contraseñas no coinciden.") #verifica que las contrasenas sean iguales,se le agrega el error de contrasenas no iguales con add_error 
        return cleaned_data


class FormularioLogin(AuthenticationForm): #SE IMPORTA VERIFICA QUE EL USUARIO EXISTA
    username = forms.CharField(
        label='Correo electrónico',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        error_messages={'required': 'Por favor ingrese un correo válido.'}
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
        error_messages={'required': 'Por favor ingrese una contraseña.'}
    )

    def clean_username(self): 
        username = self.cleaned_data.get('username') #busca al usuario
        if not username:
            raise ValidationError("Por favor ingrese un correo válido.") # si al buscar no encuenrta en la base de datos devuelva error,
        if not User.objects.filter(username=username, is_superuser=True).exists(): # se realiza para buscar al super usuario o el mismismo admin, se hace para que admin no este obligado a poner un correo
            if '@' not in username or '.' not in username:
                raise ValidationError("Por favor ingrese un correo electrónico válido.") 
        return username


    def get_invalid_login_error(self):
        return ValidationError(
            "El correo o la contraseña no son correctos.", #si los datos estan incorrectos devuelve error
            code='invalid_login',
        )

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = SolicitudContacto
        fields = ['nombre', 'apellido', 'email', 'celular', 'comentario']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo electrónico',
            'celular': 'Celular',
            'comentario': 'Comentario'
        }
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 4}),
            'celular': forms.TextInput(attrs={
                'inputmode': 'numeric',
                'pattern': '[0-9]*'
            }),
        }
        

class RespuestaContactoForm(forms.Form):
    response = forms.CharField(widget=forms.Textarea, label="Respuesta")





class FormularioAutenticacionPersonalizado(forms.Form):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Correo o Usuario'}) # no funciona el autofocus?
    )
    password = forms.CharField(
        label=("Contraseña"),
        strip=False, #no se elimnana los ' '
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}), #autocompletado contrasena
    )

    error_messages = {
        'invalid_login': (
            "El correo o la contraseña no son correctos."
        ),
        'inactive': ("Esta cuenta está inactiva."),
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password: 
            self.user_cache = authenticate(self.request, username=username, password=password) #autentica al usuario
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user): # 
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache
    

class PlatilloForm(forms.ModelForm):
    class Meta:
        model = Platillo
        fields = ['nombre', 'descripcion', 'precio', 'imagen']
        