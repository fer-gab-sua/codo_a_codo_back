document.addEventListener('DOMContentLoaded', function() {
    const dias = document.querySelectorAll('.dias')
    const listaA = document.querySelectorAll('.lista-a')

    dias.forEach((dia, index) => {
        dia.addEventListener('click', function(){
            listaA[index].classList.toggle('abierto');
        });

        document.body.addEventListener('click', function(event){
            if (event.target !== dias && event.target !== listaA[index]) {
                listasA[index].classList.remove('abierto')
            }
        });
    });
});
