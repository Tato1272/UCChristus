
# Documentación Repositorio

### Tabla de Contenidos
- Lenguajes a Instalar
- Dependencias a Instalar
- Despliegue del Repositorio
- Funciones de la Página

### Lenguajes a instalar

- Phyton 3.12.0

### Dependencias a Instalar
A continuación se muestran los comandos para instalar las dependencias necesarias:
- pip install fastapi
- pip install uvicorn

### Despliegue del Repositorio
A continuación se muestran los comandos para el Despliegue del proyecto:
- Crear_Base_de_Datos.py: Este archivo realiza la creación de la base de datos con el nombre de "ucchristus", además, de la creación de la tabla "pacientes" y el llenado de la misma a partir del archivo MOCK_DATA.json.
- uvicorn Api_Datos:app --reload: Este comando realiza el hosteo de api creada en Api_Datos para poder utilizarla más tarde.
- Live Server: Esta es una extensión de Visual Studio Code la cual sirve para el hosteo local de la página home.html y poder utilizar las funciones descritas más adelante.

### Funciones de la Página
A continuación se muestran las funciones que se pueden realizar dentro de la página:
- Buscar Paciente: lo primero que se puede realizar en la página es el "buscar paciente" el cual funciona a través de correo o id del mismo por lo que ingresando cualquiera de los 2 y presionando el botón retorna al paciente asociado al valor ingresado.
- Registrar Paciente: En este punto se puede realizar el ingreso de un paciente a la base de datos de SQLite en donde se ingresan todos los datos del paciente a excepción del ID debido a que este mismo se genera de forma automática por código.