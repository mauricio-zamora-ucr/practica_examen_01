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

def procesar_linea(texto:str) -> list[str]:
    """
    Esta función convierte una línea de texto en una lista de campos separados por
    coma. Además limpia cada campos de espacios a los extremos.
    
    """

    # paso 1
    # convertir el texto en una lista usando split
    lista:list[str] = texto.split(',')
    # paso 2
    # limpiar cada campo usando transformaciones con compresion del lista
    lista = [campo.strip() for campo in lista]
    return lista


if __name__ == '__main__':
    linea_ejemplo:str = lineas_padron[0]
    lista:list[str] = procesar_linea(linea_ejemplo)
    print(lista)