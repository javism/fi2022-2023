Cómo entregar tu práctica a través de tu web personal
=====================================================

**NOTA**: Antes de hacer estos pasos debes haber configurado tu cuenta correctamente para [alojar una web siguiendo estos pasos](../practica01/index.md).

1. Crear un proyecto Spyder "Fundamentos_Informatica" en la carpeta `www-docs/<código_aleatorio>`. Este proyecto se usará para toda la asignatura. 

1. Al abrir un nuevo módulo, debe guardarse en la carpeta del proyecto (`/home/<login>/www-docs/<código_aleatorio_anterior>/Fundamentos_Informatica/`). Por ejemplo `practica4.py` para la práctica 4.

1. En cada módulo se crearán las funciones con los comentarios de cabecera. Una vez declarada la función Spyder crea una plantilla de comentarios si introducís 3 comillas dobles seguidas y pulsáis `Alt`.

1. Al final del módulo se pondrá un `if __name__=='__main__'`, con `input('Introduce el ejercicio a ejecutar:')` y los `if-elif` correspondientes.

1. Al finalizar ejecutar el siguiente comando para establecer los permisos adecuados: `chmod -R a+rx www-docs`

1. Finalmente, crear un fichero word/pdf con los enunciados de los ejercicios, una explicación en castellano de cómo los han resuelto y el enlace al fichero `https://www.uco.es/~<login>/<código_aleatorio_anterior>/Fundamentos_Informatica/practica4.py`. 

1. **Comprueba que el enlace al módulo de Python funciona correctamente abriéndolo con tu navegador**.