from datetime import date, timedelta, datetime

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
    "901580875,119075, ,20360518,00000,AUSTIN EDUARDO                ,SIBAJA                    ,VALVERDE                  ",
]

lineas_padron2: list[str] = [
    "901550805,403007, ,20360513,00000,ALEXA DE LOS ANGELES          ,SANCHEZ                   ,MONTOYA                   ",
    "901550092,303001, ,20360204,00000,BELEN DE LA CONCEPCION        ,ROA                       ,VELASQUEZ                 ",
]


def procesar_linea(texto: str) -> list[str]:
    """
    Esta función convierte una línea de texto en una lista de campos separados por
    coma. Además limpia cada campos de espacios a los extremos.

    """

    # paso 1
    # convertir el texto en una lista usando split
    lista: list[str] = texto.split(",")
    # paso 2
    # limpiar cada campo usando transformaciones con compresion del lista
    lista = [campo.strip() for campo in lista]
    return lista


def convertir_a_fecha_ISO(texto: str) -> str:
    """
    Convierte el texto con formato YYYYMMDD en formato ISO YYYY-MM-DD.
    En caso de no tener el largo requerido devuelve 0000-00-00
    """
    if len(texto) == 8:
        yyyy: str = texto[:4]
        mm: str = texto[4:6]
        dd: str = texto[6:]
        return yyyy + "-" + mm + "-" + dd
    else:
        return "0000-00-00"


def convertir_ISO_date(iso: str) -> date:
    """
    Convierte un texto en formato ISO en un tipo fecha,
    Si hay un inconvenienet con la conversión, devuelve
    la fecha de hoy
    """
    # también hacer esto
    # return date.fromisoformat(iso)
    try:
        partes: list[str] = iso.split("-")
        numeros: list[int] = [int(parte) for parte in partes]
        return date(numeros[0], numeros[1], numeros[2])
    except Exception:
        # Si ocurre un problema (excepción) devuelve la fecha de hoy
        return datetime.now().date()


def separar_nombres(texto: str) -> tuple[str, str]:
    partes: list[str] = texto.split(" ")
    if len(partes) == 1:
        return partes[0], "N/A"
    elif len(partes) == 2:
        return partes[0], partes[1]
    else:
        return partes[0], " ".join(partes[1:])
    
def calcular_cantidad_días_entre_fechas(fecha_inicio:date, fecha_final:str) -> int:
    final:date = convertir_ISO_date(convertir_a_fecha_ISO(fecha_final))
    diferencia:timedelta = final - fecha_inicio
    return diferencia.days

def procesar_diccionario(texto:str, fecha:date) -> dict[str, int|str]:
    salida: dict[str, int|str] = {}
    campos: list[str] = procesar_linea(texto)
    
    indice_campos_requeridos:list[int] = [3,5,6,7]
    campos_seleccionado:list[str] = [campos[idx] for idx in indice_campos_requeridos]

    # calcula la cantidad de días
    dias:int = calcular_cantidad_días_entre_fechas(fecha, campos_seleccionado[0])
    salida['dias'] = dias
    # separa nombres
    primer, segundo = separar_nombres(campos_seleccionado[1])
    salida['primer_nombre'] = primer
    salida['segundo_nombre'] = segundo
    # apellidos
    salida['primer_apellido'] = campos_seleccionado[2]
    salida['segundo_apellido'] = campos_seleccionado[3]

    return salida


if __name__ == "__main__":
    # Método 01
    print('Método 01')
    linea_ejemplo: str = lineas_padron[0]
    lista: list[str] = procesar_linea(linea_ejemplo)
    print(lista)

    # Método 02
    print('Método 02')
    fecha_sin_procesar1: str = lista[3]
    fecha_sin_procesar2: str = "2026"
    fecha_convertida1: str = convertir_a_fecha_ISO(fecha_sin_procesar1)
    fecha_convertida2: str = convertir_a_fecha_ISO(fecha_sin_procesar2)
    print(fecha_sin_procesar1, fecha_convertida1)
    print(fecha_sin_procesar2, fecha_convertida2)

    # Método 03
    print('Método 03')
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

    # Método 04
    print('Método 04')
    nombre_largo = lineas_padron2[0]
    lista = procesar_linea(nombre_largo)
    print(lista[5])
    primer_nombre, segundo_nombre = separar_nombres(lista[5])
    print(f'Primer nombre {primer_nombre} y Segundo nombre {segundo_nombre}')

    # Método 05
    print('Método 05')
    inicio:date = date(2026,1,1)
    dias:int = calcular_cantidad_días_entre_fechas(inicio, fecha_sin_procesar1)
    print(f'Días {dias}')

    # Método 06
    print('Método 07')
    salida: dict[str, int|str] = procesar_diccionario(linea_ejemplo, inicio)
    print(salida)

    # Método 07
    print('Método 07')
    todas_lineas:list[str] = lineas_padron + lineas_padron2
    lista_personas:list[dict[str,str|int]] = []
    for linea in todas_lineas:
        lista_personas.append(procesar_diccionario(linea, inicio))
    
    print(lista_personas)
