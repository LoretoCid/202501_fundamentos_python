#1. Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ] 

#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz = [ [10, 15, 20], [6, 7, 14] ]

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]
#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes = [

   {"nombre": "Enrique Martin Morales", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}
#En ciudades, cambia “Cancún” por “Monterrey”
ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Monterrey"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}
coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]
#En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas = [

   {"latitud": 9.9355431, "longitud": -84.9399704}

]


#2. Iterar a través de una lista de diccionarios
#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista
#  e imprima cada llave y el valor correspondiente.

def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave} - {valor}")
            print()
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
iterarDiccionario(cantantes)

def iterarDiccionario(lista):
    for diccionario in lista:
        print(f"nombre - {diccionario['nombre']}, pais - {diccionario['pais']}")

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
iterarDiccionario(cantantes)

#3.Obtener valores de una lista de diccionarios
#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios.
# La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista.
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario.get(llave))

cantantes = [
    {"nombre": "Ricky Martin"},
    {"nombre": "Chayanne"},
    {"nombre": "José José"},
    {"nombre": "Juan Luis Guerra"}
]
iterarDiccionario2("nombre", cantantes)

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario.get(llave))
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
iterarDiccionario2("pais", cantantes)

#4. Iterar a través de un diccionario con valores de listas
#Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas.
# La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.
def imprimirInformaciín(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for valor in lista:
            print(valor)

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
imprimirInformaciín(costa_rica)