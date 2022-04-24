# ComicsStore
    Proyecto realizado para desplegar microservicios para la gestion de usuarios y algunos de sus recursos.

# Notas importantes antes de Desplegar el proyecto
    Este repositorio fue creado como demostrativo y en ningún caso deberá ser usado/compilado directo a producción, debido a que es meramente desarrollado para fines didácticos como parte de un test, aunque puede ser adaptado para ello.  

# PRODUCTION STATE

    Especificar los recursos que serán proveídos a través de:

        CORS_ORIGIN_ALLOW_ALL
        
        Ya que actualmente se encuentra con el valor: True.
        Lo puede realizar através del archivo settings.py

    Deshabilitar la opción de:

        DEBUG

        Lo puede realizar a través del archivo .env

# SECURITY

    Implementar Gestor de Tokens
    Los token generados y la gestión de ellos, sólo lo he simulado, por lo que en su lugar debería utilizarse un sistema realmente robusto como Keycloak o al menos apegarse al Estándar RFC 7519 sobre JWT :: https://www.rfc-editor.org/rfc/rfc7519.txt

    Encriptado de Datos
    Todo lo que parece estar encriptado o 'hasheado' ya sea base64 o MD5, en realidad lo incorporé al proyecto para darle más soporte apegado a lo real, se debería utilizar el mismo mecanismo que el corporativo o propietario de producto indique.

    