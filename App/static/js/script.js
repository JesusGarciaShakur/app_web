window.onload = function () {
    var currentUrl = window.location.href;
    var links = document.querySelectorAll('.navbar-nav a.nav-link, .footer a');
    for (var i = 0; i < links.length; i++) {
        if (links[i].href === currentUrl) {
            links[i].classList.add('active');
        }
    }
}
$(document).ready(function () {
    // Ocultar el encabezado al hacer scroll
    var prevScrollpos = window.pageYOffset;
    window.onscroll = function () {
        var currentScrollPos = window.pageYOffset;
        if (prevScrollpos > currentScrollPos) {
            document.querySelector(".header").style.top = "0";
        } else {
            document.querySelector(".header").style.top = "-50px"; // Ajusta este valor según el tamaño de tu encabezado
        }
        prevScrollpos = currentScrollPos;
    }
    // Mostrar el botón para volver arriba
    document.getElementById("back-to-top").style.display = "block";
});
$(document).ready(function () {
    var footer = document.querySelector('.footer');
    window.onscroll = function () {
        // Muestra el footer cuando se desplaza hasta el 80% de la página
        if (window.scrollY > document.body.scrollHeight * 0.8) {
            footer.classList.remove('footer-hidden');
        } else {
            footer.classList.add('footer-hidden');
        }
    }
});    
