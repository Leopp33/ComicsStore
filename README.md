# ComicsStore
    Proyecto realizado para desplegar microservicios para la gestion de usuarios y algunos de sus recursos.

# Notas importantes antes de Desplegar el proyecto
    Este repositorio fue creado como demostrativo y en ningún caso deberá ser usado/compilado directo a producción, debido a que es meramente desarrollado para fines didácticos como parte de un test, aunque puede ser adaptado para ello.

# Se encuentra en una version de Desarrollo: V0.7

    Funcionalidades:
        + Recibe peticiones GET a:
            
            /searchComics/
               
                Por defecto devuelve Personajes en orden alfabético.
            
            /searchComics?name
            
                Devuelve Personajes en orden alfabético.
            
            /searchComics?tittle
            
                Devuelve Comics en la estructura solicitada.
            
            + Generando una consulta a Marvel API y devolviendo resultados en forma ordenada e indentada. 
            + Registra los params name y tittle ignorando cualquier otro.
            + Por defecto lista como resultado a los personajes por orden alfabético. 
        
            + Rechaza la petición a:
                
                /

                Con un código de estado: 404

            + Cuenta con un Path base: /api/v1/

            + Se añadió soporte a:
                
                /users/ 
                
                por medio del método POST, 
            
                registrando data a través de body, 
                se comienza soporte para generar tokens.
            
        
        + Cuenta con un servidor Gunicorn (WSGI) y
        + Un servidor Nginx como Proxy Reversed o Gateway.
        + Además es posible levantar todo a través de Docker:
            +Estando posicionado en la raíz del proyecto el comando es:
                docker-compose up --build
            +Inicializará ambas imágenes en un contenedor local.
            +Por defecto, el puerto a la App es 8000, sin embargo con nginx al frente, el proyecto será accesible desde el puerto 80.
            +Si desea iniciar todo en local sin necesidad de docker, habrá que cambiar las variables de entorno a 'manuales' como lo he expresado en el archivo: settings_local.py.bak, es meramente demostrativo.   

# PRODUCTION STATE

    Especificar los recursos que serán proveídos a través de:

        CORS_ORIGIN_ALLOW_ALL
        
        Ya que actualmente se encuentra con el valor: True.
        Lo puede realizar através del archivo .env

    Deshabilitar la opción de:

        DEBUG

        Lo puede realizar a través del archivo .env

    Asegurarse del origen de los requests

        CSRF_TRUSTED_ORIGINS

        Tiene configurado localhost y http://127.0.0.1 como permitidos. 
        Lo debe modificar en el archivo .env

    Habilitar SSL

        SECURE_SSL_REDIRECT

        Una vez que se cuente con un certificado SSL y se realice la instalación de la forma apropiada, habilite esta opción pasando: True en el archivo .env


# SECURITY

    Implementar Gestor de Tokens
    Los token generados y la gestión de ellos, lo he hecho sólo en forma de simulación, por lo que en su lugar debería utilizarse un sistema realmente robusto como Keycloak o al menos apegarse al Estándar RFC 7519 sobre JWT :: https://www.rfc-editor.org/rfc/rfc7519.txt

    Encriptado de Datos
    Todo lo que parece estar encriptado o 'hasheado' ya sea base64 o MD5, en realidad lo incorporé al proyecto para darle más soporte apegado a lo real, se debería utilizar el mismo mecanismo que el corporativo donde se vaya a implementar o lo que indique el propietario del producto.

# Drivers DB

    + Se realizó prueba de migraciones, desde local y desde CLI de docker; 
        ambos para conectar con Atlas.
        + Se hace downgrade de pymongo a == 3.12.3 == ya que djongo cuenta 
        con soporte hasta esa versión, djongo queda con == 1.3.6.


# Repositorio Docker

    + Se ha publicado la imágen, de tal forma que se pueda llamar con:

        $ docker push leopp22/comicsstore_django_gunicorn:v07

        + Sin embargo, es pertinente que trabaje en conjunto con la imágen de nginx ya que éste lo he utilizado como Api Gateway.

    # Issues

    He detectado que debido a un error que genera Django al requerir las variables del archivo de configuración 'settings.py'; 
    - No se están leyendo correctamente. Esto pasa sólamente con la imágen publicada en el repositorio.
    Por ello habrá que resolverlo primero, y después intentar el 'pull'.

    +  Como alternativa, al descargar todo el código desde éste repositorio de GitHub
        
           ( https://github.com/Leopp33/ComicsStore/ )
            
            Sí es posible ejecutar todo el proyecto con docker desde el CLI en local. 

            En cuanto se haya resuelto, lo publicaré como:

                $ docker push leopp22/comicsstore_django_gunicorn:v07_fixed

    # Gracias por su Tiempo

    Siempre estaré agradecido por esta oportunidad, y por ello en forma de perfil discreto XD agradezco a todo el equipo de: Cpl.

    Tengan muy bonita semana y muy exitoso año.

    Estemos en contacto, sinceramente,

        Leo.            