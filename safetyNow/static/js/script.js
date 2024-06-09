document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    var formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    fetch('/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken  // Incluir el token CSRF
        },
        body: formData
       
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