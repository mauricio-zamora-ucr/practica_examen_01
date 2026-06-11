# Práctica 1 para examen

El examen no será así, pero si se les pedirá construir métodos. La práctica consiste en crear métodos, utilizando como base el padrón electoral del TSE.

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
Además, líneas con nombres largos:

```
901550805,403007, ,20360513,00000,ALEXA DE LOS ANGELES ,SANCHEZ ,MONTOYA 
901550092,303001, ,20360204,00000,BELEN DE LA CONCEPCION ,ROA ,VELASQUEZ 
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

lineas_padron2: list[str] = [
    "901550805,403007, ,20360513,00000,ALEXA DE LOS ANGELES ,SANCHEZ ,MONTOYA ",
    "901550092,303001, ,20360204,00000,BELEN DE LA CONCEPCION ,ROA ,VELASQUEZ ",
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
- De izquierda a derecha las posiciones se enumeran de 0, 1, 2,...., (n-1). Pero se puede también enumera de derecha a izquierda usando negativos, -1, -2, -3, etc. Donde **n** es el largo.  Por lo que se puede afirmar que la posición 0 siempre es la primera y -1 siempre es la última por ejemplo.

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

## Uso básico de para fecha, fecha-hora

Para trabajar con fechas en Python, primero debemos importar las herramientas desde el módulo nativo `datetime`: 

```python
from datetime import date, datetime, timedelta

```

### `date` (Solo Fechas)

Se usa cuando solo te importa el calendario (Año, Mes, Día), sin horas ni minutos. Es perfecto para fechas de cumpleaños o vencimientos de documentos. 

-   Creación: `date(año, mes, día)`
-   Acceso: Puedes extraer sus partes usando `.year`, `.month` o `.day`. 

```python
# Crear una fecha específica
vencimiento = date(2028, 2, 7)

print(vencimiento)        # Resultado: 2028-02-07
print(vencimiento.year)   # Resultado: 2028
print(vencimiento.month)  # Resultado: 2

```

### `datetime` y `.now()` (Fechas con Hora Exacta)

Se usa cuando necesitas precisión matemática de tiempo (Año, Mes, Día, Hora, Minuto, Segundo). Es ideal para registrar el momento exacto en que ocurre un evento.

-   `.now()`: Es un método que le pregunta al sistema operativo el reloj actual. 

```python
# Capturar el momento exacto actual
momento_actual = datetime.now()

print(momento_actual)  # Resultado aproximado: 2026-06-10 14:05:23.123456
print(momento_actual.hour) # Resultado: 14 (La hora actual)

```



### `timedelta` (Sumar y Restar Tiempo)

No representa una fecha, sino una duración o cantidad de tiempo (ej: un lapso de 5 días, 2 semanas o 3 horas). Se usa para hacer operaciones matemáticas con fechas.

-   Estructura: `timedelta(days=D, weeks=W, hours=H, minutes=M, seconds=S, )` Ver ayuda para otra fracciones de tiempo.
-   Operación: Se suma o se resta directamente a un objeto `date` o `datetime`. 

```python
hoy = date(2026, 6, 10)

# Definir un lapso de 15 días
plazo = timedelta(days=15)

# Calcular una fecha futura
fecha_pago = hoy + plazo
print(fecha_pago)  # Resultado: 2026-06-25

# Calcular una fecha pasada
hace_una_semana = hoy - timedelta(weeks=1)
print(hace_una_semana)  # Resultado: 2026-06-03

```


## Métodos solicitados (Parte 01)
Se dan parte del código, cuando vea una secuencias de **___** significa que hay que completar.

Se recomienda antes de comenzar a codificar, pensar que pasos va a realizar para completar el método, **no tiene que entregar esto**, pero use diagramas de flujo, pseudo código o simplmente escriba en un papel que pasos va a realizar.

### Método 01: Convertir cada línea de texto una lista de campos sin espacios

El método debe llamarse procesar_linea, devuelve la lista de texto y recibe un texto.



```python
def procesar_linea_______________________

linea_ejemplo:str = lineas_padron[0]
lista:_____ = procesar_linea(___________)
print(lista)

```
Respuesta
```
['101053316', '104015', '', '20280207', '00000', 'LUCILA', 'PORRAS', 'AGUERO']
```
  
### Método 02: Convertir el campo que contiene la fecha de vencimiento en formato ISO

El método debe llamarse convertir_a_fecha_ISO, devuelve un texto con el formato YYYY-MM-DD, recibe un texto con el formato YYYYMMDD.

Para este método deben usar **Slicing**.

Si el largo no es exactamente el requerido, debe devolver 0000-00-00

```python
def convertir_a_fecha_ISO_______________________

fecha_sin_procesar1:___  =  lista[3]
fecha_sin_procesar2:___  =  '2026'
fecha_convertida1: ___  =  convertir_a_fecha_ISO(fecha_sin_procesar1)
fecha_convertida2: ___  =  convertir_a_fecha_ISO(fecha_sin_procesar2)
print(fecha_sin_procesar1,fecha_convertida1)
print(fecha_sin_procesar2,fecha_convertida2)
```
Respuesta
```
20280207 2028-02-07
2026 0000-00-00
```

### Método 03: Convertir un texto fecha ISO en un date
Se debe usar el módulo de fecha hora de python, por lo que al inicio del archivo se debe colocar.
```python
# esto va al inicio del archivo .py
from datetime import date, timedelta
```
El método recibe el texto con el formato ISO y devuelve un date, en caso de válido devuelve la fecha de hoy.
```python
def convertir_ISO_date____________

print(
    fecha_convertida1,
    convertir_ISO_date(fecha_convertida1),
    type(convertir_ISO_date(fecha_convertida1)),
)

print(
    fecha_convertida2,
    convertir_ISO_date(fecha_convertida2),
    type(convertir_ISO_date(fecha_convertida2)),
)

```
Respuesta **(la fecha final varía según el día que se ejecuta el ejemplo, porque devuelve el día de hoy)**
```
2028-02-07 2028-02-07 <class 'datetime.date'>
0000-00-00 2026-06-10 <class 'datetime.date'>
```

## Métodos solicitados (Parte 02)

El profesor Stephen Goti, al analizar en detalle los campos  (columnas) del archivo del padrón, se dió cuenta que hay muchas campos que no le interesan. Por lo que esta pensando extraer solo ciertos campos y cada línea guardarlas en un diccionario, para facilitar el acceso a los campos y evitar accidentes.

Como quiere hacer análisis la distribución de nombres y apellidos. Además de los días faltantes antes del vencimiento del documento a partir del 01 de enero 2026.

Para esto hay que recordar que el orden los campos es:

```
CEDULA,CODELEC,FECHACADUC,JUNTA,NOMBRE,APELLIDO1,APELLIDO2
```
Solo se requiere los siguientes campos:
```
FECHACADUC,NOMBRE,APELLIDO1,APELLIDO2
```
Por lo que el profesor Goti quiere convertir la `FECHACADUC` en días a partir del `2026-01-01` para hacer calculos relativos a la capacidad de atención de los clientes a ver si tienen una distribución uniforme en el tiempo.

### Método 04: Separar nombres del campo nombre

El procesar los datos el profesor noto algo muy particular, que el nombre se guarda en una única columna, pero hay personas que tienen más de un nombre, por lo que tiene separar el nombre, por lo que determino 3 casos:
1. Las personas con un solo nombre.
2. Las personas con dos nombres.
3. Las raras excepciones de más de tres nombres.

Por lo que ocupa separar el nombre por los espacios en blanco que encuentre, contar las partes que se dividieron. Por lo que va seguir las siguientes reglas según la cantidad de campos:

1. Si solo tiene un campo, devuevlve 'N/A' para el segundo.
2. Si tiene dos campos.
3. Si tiene más de dos campos, devuevle para el primer campo y para el segundo campo la unión del resto de campos unidos por un espacio en blanco.


```python
def separar_nombres(______) -> tuple[str, str]:


nombre_largo  =  lineas_padron2[0]
lista  =  procesar_linea(nombre_largo)
print(lista[5])
primer_nombre, segundo_nombre  =  separar_nombres(lista[5])
print(f'Primer nombre {primer_nombre} y Segundo nombre {segundo_nombre}')

```
Resultados
```
ALEXA DE LOS ANGELES
Primer nombre ALEXA y Segundo nombre DE LOS ANGELES
```

### Método 05: Calcular los días para el vencimiento del documento

Muchos de los métodos anteriores pueden ser usado para crear métodos más complejos, por lo que va a utilizar métodos como:
- `convertir_a_fecha_ISO`
- `convertir_ISO_date`

```python
def calcular_cantidad_días_entre_fechas(fecha_inicio:date, fecha_final:str) -> ____:

inicio:date = date(2026,1,1)

dias:int = calcular_cantidad_días_entre_fechas(fecha_sin_procesar1,inicio)
print(f'Días {dias}')
```
Resultado
```
Días 767
```

### Método 06: Crear diccionario a partir de la línea

Se va a construir un diccionario con los campos (llaves):

- dias: días desde 2026-01-01 para el vencimiento del documento)
- primer_nombre
- segundo_nombre
- primer_apellido
- segundo apellido

Lo idea es hacer con un TypedDict, pero esto sería opcional. La solución se hizo con un diccionario regular.

```python
def  procesar_diccionario(texto:str, fecha:date) -> dict[str, int|str]:
    salida: dict[str, int|str] = {}
    ___
    # acá va lógica, mucha es con los métodos anteiores
    ___
    return salida

salida: dict[str, int|str] =  procesar_diccionario(linea_ejemplo, inicio)

print(salida)
```
Resultado
```
{'dias': 767, 'primer_nombre': 'LUCILA', 'segundo_nombre': 'N/A', 'primer_apellido': 'PORRAS', 'segundo_apellido': 'AGUERO'}
```
### Método 07: Unificar y cargar en una lista todos los datos de ejemplo

En este punto no hay que hacer un método, hay que ejecutarlo.
```python
todas_lineas:list[str] = lineas_padron + lineas_padron2
lista_personas:list[dict[str,str|int]] = []
for linea in todas_lineas:
    lista_personas.append(procesar_diccionario(linea, inicio))

print(lista_personas)
```
Resultado
```
[{'dias': 767, 'primer_nombre': 'LUCILA', 'segundo_nombre': 'N/A', 'primer_apellido': 'PORRAS', 'segundo_apellido': 'AGUERO'}, {'dias': 1495, 'primer_nombre': 'ANA', 'segundo_nombre': 'MARIA', 'primer_apellido': 'PEREZ', 'segundo_apellido': 'PEREZ'}, {'dias': 291, 'primer_nombre': 'GERMAN', 'segundo_nombre': 'N/A', 'primer_apellido': 'CARVAJAL', 'segundo_apellido': 'BERMUDEZ'}, {'dias': 1495, 'primer_nombre': 'JOSE', 'segundo_nombre': 'VICENTE', 'primer_apellido': 'ACUÑA', 'segundo_apellido': 'ACUÑA'}, {'dias': 454, 'primer_nombre': 'BENITIVO', 'segundo_nombre': 'N/A', 'primer_apellido': 'ARIAS', 'segundo_apellido': 'CAMPOS'}, {'dias': 3794, 'primer_nombre': 'STEPHAN', 'segundo_nombre': 'ANDRE', 'primer_apellido': 'TABUSH', 'segundo_apellido': 'PAREDES'}, {'dias': 3770, 'primer_nombre': 'SANTIAGO', 'segundo_nombre': 'DANIEL', 'primer_apellido': 'OLIVARES', 'segundo_apellido': 'FONSECA'}, {'dias': 3797, 'primer_nombre': 'DANIELA', 'segundo_nombre': 'VANESSA', 'primer_apellido': 'CHACON', 'segundo_apellido': 'AGUILAR'}, {'dias': 3794, 'primer_nombre': 'MICHELLE', 'segundo_nombre': 'MARIE', 'primer_apellido': 'PEREZ', 'segundo_apellido': 'ESPINOZA'}, {'dias': 3799, 'primer_nombre': 'NICHOLAS', 'segundo_nombre': 'N/A', 'primer_apellido': 'LOPEZ', 'segundo_apellido': 'HIDALGO'}, {'dias': 3790, 'primer_nombre': 'AUSTIN', 'segundo_nombre': 'EDUARDO', 'primer_apellido': 'SIBAJA', 'segundo_apellido': 'VALVERDE'}, {'dias': 3785, 'primer_nombre': 'ALEXA', 'segundo_nombre': 'DE LOS ANGELES', 'primer_apellido': 'SANCHEZ', 'segundo_apellido': 'MONTOYA'}, {'dias': 3686, 'primer_nombre': 'BELEN', 'segundo_nombre': 'DE LA CONCEPCION', 'primer_apellido': 'ROA', 'segundo_apellido': 'VELASQUEZ'}]
```

## Usando los aprendido responder a las siguiente inquietudes

1.  Agrupar (hacer una lista de personas), por días. Esto significa que para una misma cantidad de días, asociar una lista de personas.
2. Agrupar (hacer una lista de personas), por primer apellido. Esto significa que para un mismo apellido, asociar una lista de personas.
3. Contar cuantas personas tiene y no tienen segundo nombre.

