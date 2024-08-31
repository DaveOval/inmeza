
document.addEventListener("DOMContentLoaded", function() {
    /* Modal */
    const modal = document.getElementById('modal');
    /* BOton para cerrar */
    const closeButton = document.getElementById('close');


    setTimeout(function() {

        console.log('Mostrando el modal');

        modal.style.display = "block";

    }, 30000); 


    closeButton.onclick = function() {

        modal.style.display = "none";

    };


    window.onclick = function(event) {
        if (event.target == modal) {

            modal.style.display = "none";

        };

    };


});