
document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que el formulario se envíe de manera tradicional
    
    const serverUrl = this.dataset.serverUrl;
    const formData = new FormData(this); // Crea un objeto FormData con los datos del formulario

     // Convertir FormData a un objeto JavaScript
     const jsonData = {};
     formData.forEach((value, key) => {
         jsonData[key] = value;
     });
 
     // Convertir el objeto JavaScript a formato JSON
     const jsonString = JSON.stringify(jsonData);


    // Realiza una solicitud POST utilizando Fetch
    fetch(serverUrl + '/card', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Establecer el Content-Type a application/json
        },
        body: jsonString
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
        alert("Success");
        location.reload();
    })
    .catch(error => {
        console.error('Error en la solicitud:', error);
        // Aquí puedes manejar los errores de la solicitud
    });
});
