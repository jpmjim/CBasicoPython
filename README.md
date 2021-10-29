# Curso Básico de Python
Operadores matemáticos
----------------------
- suma 5 + 5 
- resta 7 - 2
- multiplicqación 2 * 20
- división 21 / 5
- división euclaneana 21 // 5 nos devuelve entero
- resto de la división 21 % 5 nos devuelve residuo
- portencia 2 ** 5
- raiz importamos libreria "import math" print (math.sqrt(25))

Variable
--------
- Creamos una variable " numero = 5 "
    numero es identificador de la variable
    5 es tipo de objeto en este caso es un entero
- = asignación
- == igualdad

Tipo de datos
-------------
- Números enteros 
- Números de punto flotante decimales
- Texto cadena de caracteres ('strings')
- Booleanos verdadero y falso

Convertir un dato a un tipo diferente
-------------------------------------
- input introducir datos 
- int convertimos a un número entero
- srt convertimos a texto

Operadores lógicos y de comparación
-----------------------------------
Lógicos
- and para comparar si dos valores son verdaderos.
- or para comparar si dos valores son falsos.
- not para invertir el valor booleano.

Comparación
- == Compara dos valores y te dice si son iguales o no.
- != Compara dos valores y te dice sin son diferentes o no.
- "> Compara si es mayor que otro valor.
- "> Compara si es menor que otro valor.
- ">= igual o mayor que el valor a comparar.
- <= igual o menor que el valor a comparar.

Trabajando con texto: cadenas de caracteres
--------------------------------------------
Es una función especial para un tipo de dato en particular.
nombre = 'jimmy ' 
- .upper() convertir el texto en mayúsculas
    nombre = nombre.upper() => 'JIMMY '
- .capitalize() convertir la primera letra en mayúscula
    nombre = nombre.capitalize() => 'Jimmy '
- .strip() elimina espacio que puedan estar al inicio o al final
    nombre = nombre.strip() => 'Jimmy'
- .lower() convertir a minusculas
    nombre = nombre.lower() => 'jimmy'
- .replace() reemplazar letras por otras
    nombre = nombre.replace('i', 'o' ) => 'jommy'

Indice se puede acceder a los caracteres que tiene una cadena de caracteres
- indice nombre[0]
    'j'
- len(nombre) cuanta el número de caracteres

Built-in Functions
![alt text](https://static.platzi.com/media/user_upload/Build-int%20functions-e1b3d053-5c76-4ffe-b6b3-5a61e062d77c.jpg)

Trabajando con texto: slices
----------------------------
Ejemplo:
  nombre = "Francisco"
  - nombre[0:3] o nombre[:3] => 'Fra' es una rebanada
  - nombre[3:] => 'ncisco'
  - nombre[1:7] => 'rancis'
  - nombre[1:7:2] => 'rni'  "el 2 es número de pasos que debe realizar"
  - nombre[1::3] => 'rcc' "pasos de 3 en 3"
  - nombre[::-1] => 'ocsicnarF' "nos devuelve en pasos inversos al reves"

Listas
------
Puede contener de mismo tipo o de diferente tipo son dinámicas. Se utilizan entre "[ ]"
- numeros = [1, 3, 6, 8, 9, 45, 90] 
- objetos = ['hola', 3, 4.5, True]

- objetos.append(False) => Agregar elementos a mi lista
- objetos.pop(indice) => Eliminar elementos a la lista
- for elemento in objetos => Para imprimir cada uno de los elementos 
      print(elemento)
- objetos[::-1] => tener la lista al reves
- objetos[1:3 => rango entre elementos]

Tuplas
------
Conjunto inmutable de valores ordenados eficientes son estaticos. Entre "( )"
- mi_tupla = (1, 2, 3, 4, 5) => Son estaticos no se pueden agregar ni borrar nuevos elementos