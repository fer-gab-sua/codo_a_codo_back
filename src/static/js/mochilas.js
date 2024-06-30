const borrarButtons = document.querySelectorAll('.borrar');

borrarButtons.forEach(button => {
    button.addEventListener('click', function() {
        if (confirm('¿Estás seguro de que quieres borrar esta mochila?')) {
            // Borrar la mochila
            console.log('Mochila borrada');
        }
    });
});