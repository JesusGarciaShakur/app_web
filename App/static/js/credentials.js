require('dotenv').config();

// Inicializar Firebase con las credenciales del archivo .env
const firebaseConfig = {
    apiKey: process.env.FIREBASE_API_KEY,
    authDomain: process.env.FIREBASE_AUTH_DOMAIN,
    databaseURL: process.env.FIREBASE_DATABASE_URL,
    projectId: process.env.FIREBASE_PROJECT_ID,
    storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
    messagingSenderId: process.env.FIREBASE_MESSAGING_SENDER_ID,
    appId: process.env.FIREBASE_APP_ID
};

// Inicializar Firebase
firebase.initializeApp(firebaseConfig);

// Obtener elementos del formulario
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');
const registerForm = document.getElementById('register-form');

// Escuchar el evento submit del formulario
registerForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = emailInput.value;
    const password = passwordInput.value;
    const confirmPassword = confirmPasswordInput.value;

    // Verificar que las contraseñas coincidan
    if (password !== confirmPassword) {
        alert('Las contraseñas no coinciden');
        return;
    }

    // Crear usuario con correo electrónico y contraseña
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then((userCredential) => {
            // Usuario registrado exitosamente
            var user = userCredential.user;
            alert('Usuario registrado exitosamente: ' + user.email);
        })
        .catch((error) => {
            // Error al registrar usuario
            var errorCode = error.code;
            var errorMessage = error.message;
            alert('Error al registrar usuario: ' + errorCode + ' - ' + errorMessage);
            // Verificar si el error es debido a un correo electrónico ya en uso
            if (errorCode === 'auth/email-already-in-use') {
                alert('Este correo electrónico ya está registrado');
            }
        });
});
