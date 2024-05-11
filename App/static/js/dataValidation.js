function validarFormulario() {
    let campoEmail = document.getElementById("email");
    let errorEmail = document.getElementById("email-error");
    let campoTelefono = document.getElementById("phone");
    let errorTelefono = document.getElementById("phone-error");
    let esValido = true;

    let camposRequeridos = document.querySelectorAll("input[required], textarea[required]");
    camposRequeridos.forEach(function(campo) {
        if (campo.value.trim() === "") {
            campo.nextElementSibling.style.display = "block";
            esValido = false;
        } else {
            campo.nextElementSibling.style.display = "none";
        }
    });
 
    // Validación del correo electrónico 
    if (!campoEmail.validity.valid) {
        errorEmail.style.color = "red";
        errorEmail.textContent = "Por favor, ingrese un correo electrónico válido.";
        esValido = false;
    } else {
        errorEmail.style.color = "";
        errorEmail.textContent = "";
    }
 
    // Validación del número de teléfono
    if (campoTelefono.value.length !== 10) {
        errorTelefono.style.color = "red";
        errorTelefono.textContent = "Por favor, ingrese un número de teléfono válido (10 dígitos).";
        esValido = false;
    } else {
        errorTelefono.style.color = "";
        errorTelefono.textContent = "";
    }
 
    // Alerta de campos vacíos
    if (!esValido) {
        alert("Favor de rellenar los campos.");
    }
 
    return esValido;
 }