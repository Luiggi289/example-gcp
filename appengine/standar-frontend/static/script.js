document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que el formulario se envíe de manera tradicional
    
    const formData = new FormData(this); // Crea un objeto FormData con los datos del formulario
    
    // Realiza una solicitud POST utilizando Fetch
    fetch('{{ url_for("submitted_form") }}', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la solicitud: ' + response.status);
        }
        return response.json(); // Convertimos la respuesta a JSON
    })
    .then(data => {
        console.log('Datos recibidos:', data);
        // Aquí puedes manejar la respuesta de la API
    })
    .catch(error => {
        console.error('Error en la solicitud:', error);
        // Aquí puedes manejar los errores de la solicitud
    });
});