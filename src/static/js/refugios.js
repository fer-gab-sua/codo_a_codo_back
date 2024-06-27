document.getElementById('enviarFormulario').addEventListener('click', function(event) {
    event.preventDefault(); // Evita que el formulario se envíe solo

    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    var email = document.getElementById('email').value;
    var telefono = document.getElementById('telefono').value;
    var asunto = document.getElementById('asunto').value;
    var mensaje = document.getElementById('mensaje').value;
    var aceptarDatos = document.getElementById('flexCheckDefault').checked;

    // todos los campos completos
    if (nombre === '' || apellido === '' || email === '' || telefono === '' || asunto === '' || mensaje === '') {
        alert('Por favor, complete todos los campos del formulario.');
        return; // para todo si algún campo está vacío
    }

    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Por favor, ingrese un correo electrónico válido.');
        return; // para todo si algún campo está vacío
    }

    if (!aceptarDatos) {
        alert('Por favor, acepte compartir sus datos.');
        return; // para todo si algún campo está vacío
    }
    alert('¡El formulario se envió con éxito!');
});
