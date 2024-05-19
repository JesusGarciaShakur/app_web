$(document).ready(function () {
    // Ocultar el encabezado al hacer scroll
    var prevScrollpos = window.pageYOffset;

    window.onscroll = function () {
        var currentScrollPos = window.pageYOffset;

        // Mostrar/ocultar el encabezado
        if (prevScrollpos > currentScrollPos) {
            document.querySelector(".header").style.top = "0";
        } else {
            document.querySelector(".header").style.top = "-50px"; // Ajusta este valor según el tamaño de tu encabezado
        }
        prevScrollpos = currentScrollPos;

        // Mostrar/ocultar el footer
        var footer = document.querySelector('.footer');
        if (window.scrollY > document.body.scrollHeight * 0.8) {
            footer.classList.remove('footer-hidden');
        } else {
            footer.classList.add('footer-hidden');
        }
    };

    // Mostrar el botón para volver arriba
    document.getElementById("back-to-top").style.display = "block";
});

window.onload = function () {
    var currentUrl = window.location.href;
    var links = document.querySelectorAll('.navbar-nav a.nav-link, .footer a');
    for (var i = 0; i < links.length; i++) {
        if (links[i].href === currentUrl) {
            links[i].classList.add('active');
        }
    }
};
