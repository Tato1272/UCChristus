// Traemos la tabla vacia en donde se mostraran los datos
const apiDataElement = document.getElementById('api-data');

// Definimos la url de la api a utilizar
const apiUrl = ('http://127.0.0.1:8000/obtener_datos/')

// Creamos la funcion que nos busque al paciente
function buscar() {

    // Definimos el valor por el que se filtrara 
    var valor = document.getElementById('valor').value;

    // Realizamos la solicitud a la api utilizando fetch
    fetch(apiUrl + valor)
        .then(response => {
            // Verificamos si la respuesta es exitosa
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.status}`);
            }
            // Parseamos la respuesta a un JSON
            return response.json();
        })
        .then(data => {
            // Verificamos si se encontraron pacientes
            if (data.paciente.length === 0) {
                // Mostramos una alerta en caso de que no se hayan encontrado pacientes
                alert('Paciente no encontrado');
            } else {
                // Creamos las filas de la tabla con los datos obtenidos
                const rows = data.paciente.map(paciente => {
                    return `<tr>
                    <td>${paciente[0]}</td>
                    <td>${paciente[1]}</td>
                    <td>${paciente[2]}</td>
                    <td>${paciente[3]}</td>
                    <td>${paciente[4]}</td>
                    <td>${paciente[5]}</td>
                    <td>${paciente[6]}</td>
                </tr>`;
                });

                // Agregamos las filas a la tabla
                apiDataElement.innerHTML = rows.join('');
            }
        })
        .catch(error => {
            // Manejamos los errores en caso de que se obtengan
            console.error('Hubo un error al obtener los datos:', error);
        });
}