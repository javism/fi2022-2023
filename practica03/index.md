Práctica III. Python como calculadora y tipos básicos
=====================================================

Objetivos
---------

 * Aprender a usar python en forma de calculadora
 * Identificar la consola en spyder
 * Conocer algunas instrucciones básicas de python
   * Asignar valores a variables
   * Crear expresiones aritméticas y lógicas
   * Asignar valores a variables y crear fórmulas que permitan obtener datos de figuras geométricas conocidas a partir de variables de dichas figuras. P.e. Calcular el área de un círculo a partir de su radio.
 * Observar los tipos de datos y las variables creadas en el explorador de variables de spyder

Resumen
-------

Tipos básicos: 
```python
a = 1 
a = 1.0
a = 'a'
a = True
```

Podemos usar python como una calculadora científica: 
```python
+
-
*
/
** # elevar a la potencia
% # resto de la división
```

Operadores comparación: 
```python
==
!=
<=
>=
```

Operadores lógicos. Una forma de entenderlos rápidamente es interpretarlos como multiplicación y suma binarias:  
```python
and
or
```

Precedencia de operadores y paréntesis: 
```python
1 / 2 / 4
vs 
1 / (2 / 4)
```

Ejemplos que hemos visto:
```python
1 / 2 / 4
1 / 2
(1 / 2) / 4
1 /  (2 / 4)
clear
a = 1
b = 1
a=1
a and b
a == a
a == b
( a == b ) and (1 == 2)
( a == b ) and (1 != 2)
resultado = ( a == b ) and (1 != 2)
resultado
a & b
a & 3
( a == 2 ) or ( b == 1)
( a == 2 ) or ( False )
```

Cadenas:

Todo lo que pongamos entre comillas simples o dobles se interpreta como una cadena y por tanto no se evalúa. 

```python
print("Hola mundo")
cadena = "Hola Mundo"
print(cadena) 
cadena = 'Hola Mundo'
cadena = 'Hola "Mundo"'
print('Hola 'Mundo'')
print('Hola "Mundo"')
print("Hola 'Mundo'")
```

Podemos concatenar cadenas con cadenas pero no con tipos de datos distintos. Para mezclar cadenas con enteros u otros tipos debemos aplicar una transformación. 

```python
a = 2
area = a * a
print("El área del cuadrado de lado " + a + " es igual a " + area) # Esto da un error
print("El área del cuadrado de lado " + str(a) + " es igual a " + str(area))
```

Cadenas y operadores de multiplicación (`*`) y concatenación (`+`):
```python
a = 'b'
a + 'b'
a + 'a'
a = a + 'b'
a
a = a + 'b'
a
a = a + 'b'
a
a = a + 'b'
clear
a = 'b'
a + 'b'
a + 'a'
a * 2 + 'b' * 3
2*
clear
5 * '%'
5 * '%' + './' * 3
5 * '%' + './' * 3 + '<->' *2
```

Conversión de tipos: 
```python
str(1)
str(1.0)
int('1')
float('1.0')
int('1.0')
```

Módulos de python: 

Podemos importar distintos módulos de python para tener funcionalidad extra. Por ejemplo el [módulo de matemáticas](https://docs.python.org/3/library/math.html):

```python
import math
x = 4
y = math.sin(x) + math.cos(x)
```

