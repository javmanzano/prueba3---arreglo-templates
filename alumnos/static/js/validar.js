$(document).ready(function() {
   $("#validar").validate({
       rules: {
           first_name: {
               required: true,
               minlength: 2
           },
           first_name: {
            required: true,
            minlength: 2
          },
           last_name: {
               required: true,
               minlength: 2
           },
           email: {
               required: true,
               email: true
           },
           password: {
               required: true,
               minlength: 8
           },
           confirmar_contraseña: {
               required: true,
               equalTo: "#id_password"  // Asegúrate de que el ID del campo de contraseña coincida
           },
        
           
       },
       messages: {
           first_name: {
               required: "Por favor, ingresa tu nombre.",
               minlength: "El nombre debe tener al menos 2 caracteres."
           },
           last_name: {
               required: "Por favor, ingresa tu apellido.",
               minlength: "El apellido debe tener al menos 2 caracteres."
           },
           email: {
               required: "Por favor, ingresa tu correo electrónico.",
               email: "Por favor, ingresa un correo electrónico válido."
           },
           password: {
               required: "Por favor, ingresa una contraseña.",
               minlength: "La contraseña debe tener al menos 8 caracteres."
           },
           confirmar_contraseña: {
               required: "Por favor, confirma tu contraseña.",
               equalTo: "Las contraseñas no coinciden."
           }
       },
       submitHandler: function(form) {
           form.submit();
       }
   });
});