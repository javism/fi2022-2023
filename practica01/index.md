
Práctica I. Introducción al sistema operativo Linux
===================================================

Cómo configurar tu cuenta para tu web personal en la UCO:

Recursos y enlaces
------------------

* Antes de comenzar, repasa apuntes sobre permisos de ficheros y directorios en Linux. Hay muchos muy claros, como por ejemplo este de [softzone](https://www.softzone.es/linux/tutoriales/permisos-archivos-directorios-linux/).

* Conexión remota gráfica a los servidores Linux de la Universidad de Córdoba: [Thinstation Remoto](https://www.uco.es/servicios/informatica/thinstation-remoto).

* Conexión SSH (sin interfaz gráfica) a los servidores de la UCO. Necesitas un cliente SSH, que viene de forma nativa en Linux y Mac, pero no en Windows (puedes usar [Putty](https://putty.org/)).
  * ```ssh login@ts.uco.es```
  * ```ssh -X login@ts.uco.es``` exporta la salida gráfica a tu ordenador Linux (no funciona en Windows). Con esto podrás usar el Spyder de la UCO sin tener que instalar nada más. 

* Cómo conectarte a tu carpeta para enviar y descargar archivos:
  * De forma nativa a partir de Windows 10: [How to map SFTP as a drive on Windows 10](https://sftptogo.com/blog/how-to-map-sftp-as-a-windows-10-drive/)
  * Con FileZilla: [https://filezilla-project.org/](https://filezilla-project.org/)
Pasos
-----

Abre un terminal. En este tutorial usaremos de ejemplo el login `i02samoj`. Deberás cambiar este por el tuyo. 

Crea el directorio `www-docs`:

```
mkdir www-docs
```

Asigna permisos de ejecución a tu carpeta de usuario. Esto permitirá al servidor web (otros usuarios) pasar por esta carpeta sin listar ni acceder al contenido: 

```
cd ..
chmod o+x i02samoj/
```

Vuelve a tu carpeta home y asigna los mismos permisos a `www-docs`:

```
cd
chmod  o+x www-docs
```

Vamos a comprobar que los permisos están bien configurados: 

Entra en la carpeta y crea un fichero llamado `index.html`:

```
cd www-docs
gedit index.html
```

Esto creará el fichero. Introduce el siguiente contenido, guarda y cierra el editor: 

```html
<!DOCTYPE html>
<html>
<head>
    <title>Web de ejemplo</title>
</head>
<body>
    <p>¡Hola Mundo!</p>
</body>
</html>
```

Todos los ficheros bajo ```www-docs``` o sus subdirectorios deberán tener los permisos ```o+r``` para que el servidor web pueda leerlos. Por ejemplo, para el `index.html`:

```
chmod o+r index.html
```

Todos los subdirectorios que cuelguen de ```www-docs``` deberán tener los mismos permisos ```o+x```.

Ahora abre la web [https://www.uco.es/users/TULOGIN](https://www.uco.es/users/login) o alternativamente [https://www.uco.es/~TULOGIN](https://www.uco.es/~login). Ejemplo [https://www.uco.es/~i02samoj](https://www.uco.es/~i02samoj).

Si todo va bien deberías ver una página web en blanco con el mensaje "¡Hola Mundo!". Si obtienes algún error revisa los pasos y permisos. 

Si tienes curiosidad por HTML, el lenguaje de programación básico de páginas webs, puedes empezar por este [tutorial de HTML de W3Schools](https://www.w3schools.com/html/default.asp).
