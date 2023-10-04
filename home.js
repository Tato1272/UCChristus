// Traemos la tabla vacia en donde se mostraran los datos
const tabla = document.getElementById('api-data');

// Definimos la url de la api a utilizar
const apiUrl = ('http://127.0.0.1:8000/obtener_datos/')
const apiUrl2 = 'http://127.0.0.1:8000/insertar_paciente/';

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
                document.getElementById("tabla").style.display = "block";
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
                tabla.innerHTML = rows.join('');
            }
        })
        .catch(error => {
            // Manejamos los errores en caso de que se obtengan
            console.error('Hubo un error al obtener los datos:', error);
        });
}

// Creamos la funcion para la insercion de los datos 
function insertar() {

    // Definimos de donde se extraeran los datos 
    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    var correo = document.getElementById('correo').value;
    var genero = document.getElementById('genero').value;
    var plan = document.getElementById('plan').value;
    var telefono = document.getElementById('telefono').value;

    // Realizamos la solicitud POST a la api 
    fetch(apiUrl2,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            nombre: nombre,
            apellido: apellido,
            correo: correo,
            genero: genero,
            plan: plan,
            telefono: telefono
        })
    })
    .then(response => response.json())
    .then(data => {
        // Informamos la creacion del paciente 
        alert(data.mensaje);
    })
    // Controlamos el error 
    .catch(error => {
        console.error('Hubo un error al insertar el paciente:', error);
    });
}