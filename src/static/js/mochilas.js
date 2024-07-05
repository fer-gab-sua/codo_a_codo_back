
 // Crear mochila
 $(document).ready(function() {
    // Capturar el evento de envío del formulario
    $('#registroForm').submit(function(event) {
        event.preventDefault(); // Prevenir el envío por defecto del formulario
        
        var form = $(this); // Capturar el formulario
        var url = form.attr('action'); // Obtener la URL del atributo 'action' del formulario
        
        $.ajax({
            type: 'POST',
            url: url,
            data: form.serialize(), // Serializar los datos del formulario para enviarlos
            success: function(response) {
                if (response.status === 'success') {
                    $('#mochilas-container').empty().append(response.html);
                    $('#nombre_mochila').val(''); // Limpiar el campo de cantidad
                    $('#descripcion_mochila').val(''); // Limpiar el campo de contenido
                } else {
                    alert('Error al crear la mochila: ' + response.message);
                }
            },
            error: function(xhr, status, error) {
                alert('Error al crear la mochila: ' + xhr.responseText);
            }
        });
    });
});
// Eliminar mochila
$(document).on('submit', '.delete-mochila-form', function(event) {
    event.preventDefault(); // Previene el comportamiento por defecto del formulario
    const mochilaId = $(this).data('mochila-id');
    const url = $(this).data('url');

    $.ajax({
        type: 'POST',
        url: url,
        data: $(this).serialize(),
        success: function(response) {
            if (response.status === 'success') {
                $('#mochilas-container').empty().append(response.html);
                $('#Mochila-Seleccionada').empty()

            }
        },
        error: function() {
            alert('Error al eliminar la mochila');
        }
    });
});

// Seleccionar mochila para ver detalles (delegación de eventos)
$(document).on('submit', '.select-mochila-form', function(event) {
    event.preventDefault(); // Prevenir el comportamiento por defecto del formulario
    const mochilaId = $(this).data('mochila-id');
    const url = $(this).data('url');
    
    $.ajax({
        type: 'POST',
        url: url,
        success: function(response) {
            if (response.status === 'success') {
                $('#Mochila-Seleccionada').empty().append(response.html); // Actualiza la sección de detalles de la mochila seleccionada
            }
        },
        error: function() {
            alert('Error al seleccionar la mochila');
        }
    });
});




$(document).ready(function() {
    // Capturar el evento de envío del formulario para registrar un nuevo item
    $(document).on('submit', '#registroFormItem', function(event) {
        event.preventDefault(); // Prevenir el comportamiento por defecto del formulario
        
        // Obtener los datos del formulario
        const mochilaId = $(this).data('mochila-id');
        const url = $(this).data('url');
        // Enviar la solicitud AJAX
        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(), // Serializar datos del formulario para enviarlos
            success: function(response) {
                if (response.status === 'success') {
                    // Actualizar la sección de detalles de la mochila seleccionada
                    $('#Mochila-Seleccionada').empty().append(response.html);
                    $('#cantidad').val(''); // Limpiar el campo de cantidad
                    $('#contenido').val(''); // Limpiar el campo de contenido
                } else {
                    alert('Error al agregar el item');
                }
            },
            error: function() {
                alert('Error al agregar el item');
            }
        });
    });
});








$(document).ready(function() {
    // Manejar el evento de envío del formulario para eliminar un item
    $(document).on('submit', '.delete-item-form', function(event) {
        event.preventDefault(); // Prevenir el comportamiento por defecto del formulario

        const itemId = $(this).data('item-id');
        const url = $(this).data('url');


        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),
            success: function(response) {
                if (response.status === 'success') {
                    $('#item-' + itemId).remove();
                } else {
                    alert('Error al eliminar el item');
                }
            },
            error: function() {
                alert('Error al eliminar el item');
            }
        });
    });
});

