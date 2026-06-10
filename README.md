# Práctica 1 para examen

## Contexto

El profesor Stephen Goti del curso Indroducción al Análisis de Datos 1, los ha buscado para que le ayuden a realizar unos ejercicios muy realistas para dar ejemplos en clases. El profesor quiere usar el dataset del Tribunal Supremo de Elecciones (TSE) del padrón electoral del país [Ver página de descarga del padrón electoral](https://www.tse.go.cr/descarga_padron.html) . 

Al revisar el padrón se dio cuenta que los datos no están como los requiere y necesita cierto procesamiento previo, por lo que necesita que le ayuden a diseñar algunas funciones en python. Estás deben ir documentadas en docstring.

El día  2026-10-06, el profesor descargo el padrón del país. Y tomó las primeras 5 líneas y las últimas líneas del archivo, para usarlas como ejemplo para que práctiquen. 

El profesor identifico el nombre de cada columna, son los siguientes:
```
CEDULA,CODELEC,FECHACADUC,JUNTA,NOMBRE,APELLIDO1,APELLIDO2
```

Primeras 5 líneas:
```
101053316,104015, ,20280207,00000,LUCILA                        ,PORRAS                    ,AGUERO                    
101240037,823001, ,20300204,00000,ANA MARIA                     ,PEREZ                     ,PEREZ                     
101280947,103008, ,20261019,00000,GERMAN                        ,CARVAJAL                  ,BERMUDEZ                  
101290149,101010, ,20300204,00000,JOSE VICENTE                  ,ACUÑA                     ,ACUÑA                     
101290354,104014, ,20270331,00000,BENITIVO                      ,ARIAS                     ,CAMPOS                    
```

Últimas 5 líneas:
```
901580633,819001, ,20360522,00000,STEPHAN ANDRE                 ,TABUSH                    ,PAREDES                   
901580685,407003, ,20360428,00000,SANTIAGO DANIEL               ,OLIVARES                  ,FONSECA                   
901580698,814004, ,20360525,00000,DANIELA VANESSA               ,CHACON                    ,AGUILAR                   
901580721,814003, ,20360522,00000,MICHELLE MARIE                ,PEREZ                     ,ESPINOZA                  
901580735,103006, ,20360527,00000,NICHOLAS                      ,LOPEZ                     ,HIDALGO                   
901580875,119075, ,20360518,00000,AUSTIN EDUARDO                ,SIBAJA                    ,VALVERDE                  
```

Python:
```python
# Arreglo de strings para cada línea del padrón, para ser usado en las prácticas
lineas_padron: list[str] = [
    "101053316,104015, ,20280207,00000,LUCILA                        ,PORRAS                    ,AGUERO                    ",
    "101240037,823001, ,20300204,00000,ANA MARIA                     ,PEREZ                     ,PEREZ                     ",
    "101280947,103008, ,20261019,00000,GERMAN                        ,CARVAJAL                  ,BERMUDEZ                  ",
    "101290149,101010, ,20300204,00000,JOSE VICENTE                  ,ACUÑA                     ,ACUÑA                     ",
    "101290354,104014, ,20270331,00000,BENITIVO                      ,ARIAS                     ,CAMPOS                    ",
    "901580633,819001, ,20360522,00000,STEPHAN ANDRE                 ,TABUSH                    ,PAREDES                   ",
    "901580685,407003, ,20360428,00000,SANTIAGO DANIEL               ,OLIVARES                  ,FONSECA                   ",
    "901580698,814004, ,20360525,00000,DANIELA VANESSA               ,CHACON                    ,AGUILAR                   ",
    "901580721,814003, ,20360522,00000,MICHELLE MARIE                ,PEREZ                     ,ESPINOZA                  ",
    "901580735,103006, ,20360527,00000,NICHOLAS                      ,LOPEZ                     ,HIDALGO                   ",
    "901580875,119075, ,20360518,00000,AUSTIN EDUARDO                ,SIBAJA                    ,VALVERDE                  "
]
```


El profesor Goti, preocupado para que puedan realizar sus labores de forma más sencilla decició darles pequeñas guías a lo largo de la práctica para ustedes puedan implementar los métodos de forma sencilla. 

## Manipulación básica de Listas y Strings


### Métodos Esenciales de Strings
Métodos nativos para limpiar y unir o "romper" texto a través de uno o varios carácteres.

-   `.strip()`: Borra los espacios en blanco tanto al inicio como al final del texto.
-   `.lstrip()`: Borra los espacios en blanco solo a la izquierda (inicio).
-   `.rstrip()`: Borra los espacios en blanco solo a la derecha (final).

```python
texto = "   LUCILA   "
# Limpieza de espacios
print(texto.strip())   # Resultado: "LUCILA"
print(texto.lstrip())  # Resultado: "LUCILA   "
print(texto.rstrip())  # Resultado: "   LUCILA"

```

-   `.split(separador)`: Rompe un string en varias partes basándose en un carácter y devuelve una lista.
-   `conector.join(lista)`: Une los elementos de una lista de texto usando un conector.

```python
# Romper y Unir
datos = "101053316,104015,20280207"
lista_datos = datos.split(",")  # Resultado: ['101053316', '104015', '20280207']

nombres = ["Ana", "Maria"]
print("-".join(nombres))        # Resultado: "Ana-Maria"

```

### List Comprehension (Comprensión de Listas) 

Es una forma corta y elegante de crear una nueva lista transformando los elementos de otra. 

-   Estructura: `nueva_lista = [transformacion for elemento in origen]`
-   💡 Recuerda: Los `strings` actúan como listas de caracteres. Puedes recorrerlos de la misma manera.

```python
# Ejemplo 1: Elevar números al cuadrado
numeros = [1, 2, 3]
cuadrados = [x**2 for x in numeros]  # Resultado: [1, 4, 9]

# Ejemplo 2: Modificar texto (El string se comporta como lista)
palabra = "hola"
letras_mayusculas = [letra.upper() for letra in palabra]  
# Resultado: ['H', 'O', 'L', 'A']

```

### Slicing (Rebanado)

El _slicing_ te permite extraer una porción o "rebanada" de una estructura utilizando sus índices numéricos.

-   Estructura: `objeto[inicio:fin]` _(Nota: El índice de `fin` no se incluye en el resultado)_.
-   💡 Recuerda: Funciona exactamente igual en listas y en cadenas de texto (`strings`).

```python
# Ejemplo con Listas
frutas = ["manzana", "pera", "uva", "mango"]
mis_frutas = frutas[1:3]  # Resultado: ['pera', 'uva']

# Ejemplo con Strings
fecha = "20280207"
año = fecha[0:4]   # Resultado: "2028"
mes = fecha[4:6]   # Resultado: "02"
dia = fecha[6:8]   # Resultado: "07"

```

### El uso de `len()`

La función `len()` devuelve la cantidad total de elementos que tiene una estructura.

-   En una lista, cuenta cuántos objetos contiene.
-   En un string, cuenta cuántos caracteres tiene (incluyendo espacios y signos). [5]

```python
# Tamaño de lista
colores = ["rojo", "azul", "verde"]
print(len(colores))  # Resultado: 3

# Tamaño de string
nombre = "JUAN CARLOS"
print(len(nombre))   # Resultado: 11 (Cuenta el espacio en blanco)

```

## Métodos solicitados (Parte 01)


  
