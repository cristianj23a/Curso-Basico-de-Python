# Curso Básico de Python

## Módulo 1 Introducción a la programación con Python

### Clase 1 El arte de la programación

Python tiene una forma de escribir elegante y simple.
La programación es dar solución tecnológica a distintos problemas y en el mercado laboral la demanda de programadores es alta.

### Clase 2 ¿Por qué Python?

Python es multiplataforma y se adapta a distintos tipos de soluciones como en Inteligencia artificial, Backend, Data Sience, Videos Juegos y Desarrollo Móvil.

- **Frontend**: Se encarga de llegar el diseño de un sistema a la realidad.
- **IOT**: (Internet de las cosas): Se encarga de conectarse a internet a elementos como electrodomésticos, robots, etc.
- **Inteligencia Artificial**: Enseña a la computadora en aprender a resolver un problema sin que una persona intervenga.
- **Backend**: Se crear la lógica para que el sistema funcione.
- **DevOps**: controla la infraestructura donde funciones la aplicación.
- **Data Sience**: Toma los datos de la entidad y genera información valiosa como para aumentar la eficacia de un negocio o empresa.
- **Video Juegos**: Es una combinación de arte, programación y entretenimiento para generar una buena experiencia de usuario.
- **Desarrollo Móvil**: Crean aplicaciones que viven en la play store para brindar distintos tipos de soluciones o experiencias de usuarios.


Una de las muchas ventajas que tiene python es la buenas prácticas, código elegante y de fácil entendimiento.

### Clase 3 El núcleo de un programa: los algoritmos

Algoritmo: 
- Es una conjunto de pasos para resolver un problema
- Los pasos son finitos
- No ambiguo

### Clase 4 Instalación de nuestras herramientas

Para programar se necesita las siguientes herramientas:

- Editor de código como Visual Studio Code, Sublime,Atom, Pycharm, etc.
https://code.visualstudio.com/download

- Consola, puede realizar un conjunto de tareas y las herramientas son cmd, shell, cmder, etc.
https://cmder.net/

- Instalación de python 
https://www.python.org/downloads/

### Clase 7 Tu mejor herramienta: la consola

cls o CTRL + L: limpiar consola
cd: ruta de la carpeta
ls: saber que archivos hay en la carpeta
mkdir nombre: crear carpeta
touch nombre: Crear archivo

## Módulo 2 Conceptos básicos de Python

### Clase 8 Explorando Python: operadores aritméticos
Python obedece la reglas matematicas, por ejemplo si 5 + 5 * 2 dara como resultado 15.
Ejmp:
```
λ python3
Python 3.8.7 (default, Jan 18 2021, 21:09:34)  [GCC 10.2.0 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 5 + 5
10
>>> print(5 + 5)
10
>>> 5 - 5
0
>>> 20+5*10
70
>>> 5*4*3*2*1
120
>>> 21 // 5
4
>>> 21 % 5
1
>>> 2**2
4
>>> 2**3
8
>>> 5 + 5 * 2
15
```

### Clase 9 ¿Qué es una variable?

Es una caja donde se puede guardar objetos: números, texto, etc.
```
λ python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> numero = 3
>>> print(numero)
3
>>> num = 1
>>> num2= 2
>>> num3= 3
>>> print(num, num2, num3)
1 2 3
>>> res = num + num2 + num3
>>> print(res)
6
>>> num + num2 + num3
6
>>> res
6
```

### Clase 10 Los primitivos: tipos de datos sencillos

Tanto como python o cualquier lenguaje de programación tiene 4 tipos de datos principales:

1.- Números Enteros
2.- Números Flotante
3.- Texto o String (Cadena de Caracteres)
4.- Booleanos (Verdadero o Falso)

```
λ python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> nombre = "Cristian"
>>> nombre
'Cristian'
>>> nombre2 = "Jorge"
>>> nombre2
'Jorge'
>>> nombre + nombre2
'CristianJorge'
>>> nombre + " " + nombre2
'Cristian Jorge'
>>> nombre * 4
'CristianCristianCristianCristian'
>>> nombre + " " * 4
'Cristian    '
>>> (nombre + " ") * 4
'Cristian Cristian Cristian Cristian '
>>> num_decimal = 3.4
>>> num_decimal
3.4
>>> es_estudiante = True
>>> es_estudiante
True
>>> print(es_estudiante)
True
```

### Clase 11 Convertir un dato a un tipo diferente

```
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> num1 = input("Escribe un número: ")
Escribe un número: 4
>>> num1
'4'
>>> num2 = input("Escribe un número: ")
Escribe un número: 5
>>> num2
'5'
>>> num1 + num2
'45'
>>> num1 = int(num1)
>>> num1
4
>>> num2 = int(num2)
>>> num2
5
>>> num1 + num2
9
>>> num_dec = 4.5
>>> int(num_dec)
4
>>> num_dec
4.5
>>> str(num_dec)
'4.5'
```

### Clase 11 Convertir un dato a un tipo diferente

Los operadores son : And, Or, Not, ==, !=, >, <, >=, <=.

and para comparar si dos valores son verdaderos.
-or para comparar si dos valores son falsos.
-not para invertir el valor booleano.
-== Compara dos valores y te dice si son iguales o no.
-!= Compara dos valores y te dice sin son diferentes o no.
-> Compara si es mayor que otro valor.
-> Compara si es menor que otro valor.
>= igual o mayor que el valor a comparar.
<= igual o menor que el valor a comparar.

```
>>> est = True
>>> est
True
>>> trab = False
>>> trab
False
>>> est and trab
False
>>> est or trab
True
>>> not est
False
>>> not trab
True
>>> num1= 5
>>> num2= 5
>>> num1 == num2
True
>>> num3= 7
>>> num1 == num3
False
>>> num1 != num3
True
>>> num1 > num3
False
>>> num1 < num3
```

### Clase 12 Tu primer programa: conversor de monedas

```
soles = input("¿Cuántos soles tienes?: ")
soles = float(soles)
valor_dolar = float(3.95)
dolares = soles * valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
```

## Módulo 3 Herramientas para programar

### Clase 13 Construyendo el camino de un programa con condicionales

```
edad = int(input("Escribe tu edad: "))
if edad > 17:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

numero = int(input('Escribe un número: '))

if numero > 5:
    print('Es mayor a 5')
elif numero == 5:
    print('El igual a 5')
else:
    print('Es menor a 5')
```

### Clase 14 Varios países en mi conversor de monedas

```
menu = """
Bienvenido al conversor de monedas 💰

1 - Soles
2 - Pesos colombianos
3 - Pesos argentinos
4 - Pesos mexicanos
Elige una opicón: """

opcion = input(menu)

if opcion == 1:
    soles = input("¿Cuántos soles tienes?: ")
    soles = float(soles)
    valor_dolar = float(3.95)
    dolares = soles * valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

elif opcion == 2:
    soles = input("¿Cuántos Pesos colombianos tienes?: ")
    soles = float(soles)
    valor_dolar = float(970.33)
    dolares = soles * valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

elif opcion == 3:
    soles = input("¿Cuántos Pesos argentinos tienes?: ")
    soles = float(soles)
    valor_dolar = float(24.25)
    dolares = soles * valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

elif opcion == 4:
    soles = input("¿Cuántos Pesos mexicanos tienes?: ")
    soles = float(soles)
    valor_dolar = float(5.03)
    dolares = soles * valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

else:
    print('Por favor ingresa la opción correcta')
```

### Clase 15 Aprendiendo a no repetir código con funciones

Para evitar repetir el mismo codigo, podemos usar la función "def" que sirve para reutilizar el mismo codigo.

```
def conversacion(mensaje):
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opción (1,2,3): '))
if opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion == 3:
    conversacion('Elegiste la opción 3')
else:
    print('Escribe la opción correcta')
```

### Clase 16 Modularizando nuestro conversor de monedas

```
def conversor(tipo_moneda, valor_dolar):
    moneda = input("¿Cuántos " + tipo_moneda + " tienes?: ")
    moneda = float(moneda)
    dolares = moneda * valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Soles
2 - Pesos colombianos
3 - Pesos argentinos
4 - Pesos mexicanos
Elige una opicón: """

opcion = int(input(menu))

if opcion == 1:
    conversor("soles", 3.95)
elif opcion == 2:
    conversor("pesos colombianos", 0.00026)

elif opcion == 3:
    conversor("pesos mexicanos", 0.010)

elif opcion == 4:
    conversor("pesos argentinos", 0.05)

else:
    print('Por favor ingresa la opción correcta')
```

### Clase 17 Trabajando con texto: cadenas de caracteres

upper: Sirve para poner em mayuscula los texto y la sintaxis es texto.upper().
Capitalize: Sirve para convertir la primera letra en mayuscula y el resto en minuscula, la sintaxis es texto.capitalize().
strip: Sirve para quitar los espacios de un texto, la sintaxis es texto.strip().
lower: Sirve para convertir todos los textos a minuscula, la sintaxis es texto.lower().
replace: Sirve para reemplazar textos, la sintaxis es texto.replace().
[numero]: sirve para acceder al texto de una palabra, la sintaxis es texto[0] con este codigo accedes a la primera letra del texto.
len: Sirve para contar la cantidad de letras en una palabra, la sintaxis es len(texto).

```
¿Cuál es tu nombre?: Cristian
>>> nombre.upper()
'CRISTIAN'
>>> nombre.capitalize()
'Cristian'
>>> nombre
'Cristian'
>>> nombre = nombre.capitalize()
>>> nombre
'Cristian'
>>> nombre = input("¿Cuál es tu nombre?: ")
¿Cuál es tu nombre?: cristian
>>> nombre
'cristian '
>>> nombre = nombre.capitalize()
>>> nombre
'Cristian '
>>> nombre = nombre.strip()
>>> nombre
'Cristian'
>>> nombre = nombre.lower()
>>> nombre
'cristian'
>>> nombre = nombre.replace('o', 'a')
>>> nombre
'cristian'
>>> nombre = nombre.replace('a', 'o')
>>> nombre
'cristion'
>>> nombre[0]
'c'
>>> len(nombre)
8
```

### Clase 18 Trabajando con texto: slices

La slice son para particionar un texto y leer el orden deseado.

```
>>> nombre = "Cristian"
>>> nombre
'Cristian'
>>> nombre[0]
'C'
>>> nombre[0:3]
'Cri'
>>> nombre[:3]
'Cri'
>>> nombre[3:]
'stian'
>>> nombre[1:7]
'ristia'
>>> nombre[1:7:2]
'rsi'
>>> nombre[1:7:3]
'rt'
>>> nombre[::-1]
'naitsirC'
```

### Clase 19 Proyecto: palíndromo

En este proyecto vamos a crear un proyecto para identificar los palindromo.
Un palindromo es una palabra o frase que se lee igual en un sentido que en otro. Ejmp:

luz azul

```
def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
     palabra = input('Escribe una palabra: ')
     es_palindromo = palindromo(palabra)
     if es_palindromo == True:
         print('Es palíndromo')
     else:
         print('No es palíndromo')

if __name__ == '__main__':
    run()
```

## Módulo 4 Bucles

### Clase 20 Aprendiendo bucles

```
contador = 0
print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador)) 
contador = 1
print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador)) 
contador = 2
print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador)) 
contador = 3
print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador)) 
contador = 4
print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador)) 
```

### Clase 21 El ciclo while

While: permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición.

Las contantes se declaran en mayuscula.

```
def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()
```

### Clase 22 Explorando un bucle diferente: el ciclo for

```
for: es un bucle que tiene la misma función de while pero con una sintaxis de menos codigo.

 for contador in range(1,1001):
     print(contador)

for i in range(1,11):
    print(11*i)
```

### Clase 23 Recorriendo un string con for

```
def run():
    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())

if __name__ == '__main__':
    run()
```

### Clase 24 Interrumpiendo ciclos con break y continue

break: cancela la ejecución del programa hasta la linea donde se declaro el break.
continue: salta las lineas de condigo de abajo hasta que se dija lo contrario.

```
def run():
    # for contador in range(100):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()
```

### Clase 25 Proyecto: prueba de primalida

```
def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    run()
```

### Clase 26 Proyecto: videojuego

```
import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número mas grande')
        else:
            print('Busca un número menor')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!')

if __name__ == '__main__':
    run()
```

## Módulo 5 Estructuras de datos

### Clase 27 Almacenar varios valores en una variable: listas

listas: pueden almacenar tantos valores como desees con cualquier tipo de datos.

```
>>> numeros = [1,2,3,5,76]
>>> numeros
[1, 2, 3, 5, 76]
>>> objetos = ['hola',2,4.5,True]
>>> objetos
['hola', 2, 4.5, True]
>>> objeto[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'objeto' is not defined
>>> objetos[1]
2
>>> objetos.append(False)
>>> objetos
['hola', 2, 4.5, True, False]
>>> objetos.pop(1)
2
>>> objetos
['hola', 4.5, True, False]
```

### Clase 28 Entendiendo cómo funcionan las tuplas

Las tuplas son un tipo de datos estatico, lo cual significa que no se puede agregar o eliminar datos. La ventaja sobre las listas es que el recorrido es mucho mas rapido.

```
>>> mi_tupla = (1,2,3,4,5)
>>> mi_tupla
(1, 2, 3, 4, 5)
>>> for numero in mi_tupla:
...     print(numero)
...
1
2
3
4
5
```

### Clase 29 ¿Qué son los diccionarios?

Es una estructura de valores de llaves y datos, el acceso a estos datos es a traves de las llave unicas.

```
def run():
    mi_diccionario = {
        'llave1':1,
        'llave2':2,
        'llave3':3,
    }
    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brazil': 210147125,
        'Colombia': 50372424,
    }

    print(poblacion_paises['Argentina'])

    for pais in poblacion_paises.keys():
        print(pais)

    for pais in poblacion_paises.values():
        print(pais)

    for pais in poblacion_paises.items():
        print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes ')



if __name__ == '__main__':
    run()
```

### Clase 30 Proyecto: generador de contraseñas

```
import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C','D','F','G']
    minusculas  = ['a','b','c','d','f','g']
    simbolos = ['!','#','$','&','/','(',')']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = ''.join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)

if __name__ == '__main__':
    run()
```
