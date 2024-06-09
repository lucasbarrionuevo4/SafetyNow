document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Aquí, deberías enviar los datos a tu servidor para verificar las credenciales
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = 'home';  // Redirige a la página de inicio si el inicio de sesión es exitoso
        } else {
            alert('Usuario o contraseña incorrectos.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});