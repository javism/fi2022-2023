Práctica IV. Entrada y salida de datos
======================================

- [Práctica IV. Entrada y salida de datos](#práctica-iv-entrada-y-salida-de-datos)
  - [Salida en Python por el terminal](#salida-en-python-por-el-terminal)
  - [Entrada por teclado](#entrada-por-teclado)
  - [Lectura y escritura de ficheros](#lectura-y-escritura-de-ficheros)
  - [Plantilla Python para entregar la práctica](#plantilla-python-para-entregar-la-práctica)

Salida en Python por el terminal
--------------------------------
Entrada y Salidade la documentación oficial (se puede elegir idioma en): [7. Entrada y Salida](https://docs.python.org/es/3/tutorial/inputoutput.html). Tienes ejemplos más avanzados en [Real Python](https://realpython.com/python-print/).
Entrada y Salidacadenas**. Manipulando cadenas manualmente usando la concatenación, funciones de conversión... Así lo hemos hecho hasta ahora. 


```python
a = 4
print('El tipo de la variable a es ' + str(type(a)) + ' y su valor es ' + str(a) )
```

**Literales de cadena** o **f-strings**.
```python
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
```

Podemos especificar la precisión en números flotantes.  
```python
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
```


**str.format()**

```python
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
'{:-10} YES votes  {:2.4%}'.format(yes_votes, percentage)
```


Entrada por teclado
-------------------

Lee del teclado y lo guarda como tipo `str` en la variable nombre

```python
nombre = input('Introduce tu nombre:')
print(f'Hola, te llamas {nombre}')
print('Hola, te llamas ' + nombre)
```

Si queremos leer números tenemos que transformarlos con `int()`, `float()` para convertir al tipo adecuado....

```python
x = int(input('Introduce tu código postal:'))
print(type(x))
x + 2
```

Lectura y escritura de ficheros
-------------------------------

Estos ejemplos se basan en la documentación oficial:  [7.2. Leyendo y escribiendo archivos¶](https://docs.python.org/es/3/tutorial/inputoutput.html#reading-and-writing-files)

**Es importante leer las implicaciones de usar `with` para asegurar que se llama al método `close()` de forma adecuada.**

```python
# Abre un fichero en modo texto para escritura
# Alternativamente, si usamos 'a' en vez de 'w' 
# los datos nuevos se añaden al final del fichero.
# \n es el carácter de salto de línea
with open('datos.txt', 'w') as f:
    f.write('Hola \n') 
    f.write(' mundo')
    f.write(str(56)) # Sólo se pueden escribir cadenas

# Abre el fichero de texto en modo lectura y lo lee entero y guarda en la variable contenido_fichero
with open('datos.txt', 'r') as f: 
    contenido_fichero = f.read()
    
print(contenido_fichero)
```

Plantilla Python para entregar la práctica
------------------------------------------

Puedes descargar el código de ejemplo de la práctica 4 que estuvimos desarrollando en clase: [practica4.py](practica4.py)