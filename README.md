# test_emqu

#### Luego de clonar el repo, se deberá crear el entorno virtual dentro de la misma carpeta con el comando: *python -m venv nombreDeseadoDelEntorno*
#### Ahora se procede a activar el entorno ejecutando *nombreDeseadoDelEntorno/Scripts/activate* (en caso de linux se cambia Scripts por bin)
#### Posteriormente se procede a instalar los paquetes necesarios para ejecutar la aplicación, esto será a partir del archivo *requirements.txt* que se encuentra en la raiz del repo, ejecutaremos el comando *pip install -r requirements.txt*
#### Se procede a ejecutar las migraciones con los comandos *python manage.py makemigrations* y *¨python manage.py migrate*
#### Se ejecuta el servidor con *python manage.py runserver*

## Rutas de la API
### *'api/1.0/usuarios'* para el listado (GET) y la creación (POST) de usuarios
##### para el post se envia un json con los datos nombre, apellido y correo, todos son strings
### *'api/1.0/usuarios/<int:usuario_id>'* para la edición y eliminación de usuarios
### *'api/1.0/equipos'* para el listado (GET) y la creación (POST) de equipos
##### para el post se envia un json con los datos nombre, modelo y direccionIp, todos son strings
### *'api/1.0/equipos/<int:equipo_id>'* para la edición y eliminación de equipos
### *'api/1.0/pruebas'* para el listado (GET) y realización (POST) de pruebas de ping
##### para el post se envia un json con los datos equipo (es un entero correspondiente a un id de equipo) y usuario (es un entero correspondiente a un id de usuario)
##### el dato equipo corresponde es una llave foranea del equipo al que se le realiza la prueba de ping, y el dato usuario es una llave foranea del usuario que realiza la prueba
