# IG BOT

## Descripción

IG BOT es una aplicación diseñada para obtener datos de seguidores y seguidos de perfiles de Instagram, incluyendo nuestro propio perfil. La funcionalidad principal de la aplicación es identificar quién nos ha dejado de seguir y las personas que seguimos pero que no nos siguen de vuelta.

## Funcionalidades

- Obtener datos de seguidores y seguidos de cualquier perfil de Instagram.
- Identificar quién ha dejado de seguirte.
- Identificar las personas a las que sigues pero que no te siguen de vuelta.

## Requisitos

Para ejecutar IG BOT, necesitas instalar las siguientes librerías y herramientas:

- Python (versión 3.6 o superior)
- [Selenium](https://www.selenium.dev/)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) (para Firefox)
- Firefox Web Browser

## Instalación

1. Clona el repositorio a tu máquina local:
    ```sh
    git clone https://github.com/tuusuario/ig-bot.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd ig-bot
    ```
3. Instala las dependencias necesarias:
    ```sh
    pip install selenium
    ```

4. Descarga y ubica el ejecutable de Geckodriver en tu PATH. Puedes descargarlo desde [aquí](https://github.com/mozilla/geckodriver/releases).

## Uso

1. Ejecuta el script `test.py`:
    ```sh
    python test.py
    ```

2. Sigue las instrucciones en la consola para ingresar tus credenciales de Instagram y los perfiles que deseas analizar.

## Notas

- Asegúrate de que Firefox esté instalado y actualizado en tu máquina.
- La aplicación utiliza Selenium para automatizar la navegación y obtención de datos desde Instagram.
- Tu cuenta de Instagram puede requerir autenticación adicional (como códigos de verificación) cuando uses la aplicación por primera vez.
- La opción 2 no funciona bien del todo debido a la implementación propia de la web de Instagram
- No cerrar el navegador ni minimizar mientras se ejecuta
