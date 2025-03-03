#Multiplica por 2: 
# crea una función que reciba un número y devuelva una lista que contenga los números enteros multiplicados por dos,
# desde el 0 hasta el número proporcionado como entrada. Ejemplo: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]
def multiplica_por_2(num):
    return [i * 2 for i in range(num + 1)]
resultado = multiplica_por_2(4)
print(resultado) # Imprime [0, 2, 4, 6, 8]

#Suma y resta: crea una función que reciba una lista con dos números. 
#Imprime la suma de los dos números y regresa la resta de los dos números.
#Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1
def suma_y_resta(lista):
    suma = sum(lista)  
    resta = lista[0] - lista[1] 
    print(suma)  
    return resta  
resultado = suma_y_resta([5, 4])
print(resultado) # Imprime 9 y regresa 1

#Sumatoria menos longitud: crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.
#Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)
def sumatoria_menos_longitud(lista):
    sumatoria = sum(lista)
    longitud = len(lista)
    return sumatoria - longitud
resultado = sumatoria_menos_longitud([1, 2, 3, 4])
print(resultado) # Imprime 6

#Valores multiplicados por el segundo: 
# Escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. 
# Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.
#Ejemplo: valores_multiplicados_segundo([1, 3, 5, 7]) debe imprimir 4 y devolver [3, 9, 15, 21]
#Ejemplo: valores_multiplicados_segundo([1]) debe imprimir 1 y devolver [ ]

def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        return [] 
    segundo = lista[1]
    nueva_lista = [x * segundo for x in lista]
    print(len(lista))
    return nueva_lista

resultado = valores_multiplicados_segundo([1, 3, 5, 7])
print(resultado)  # Imprime 4 y devolverá [3, 9, 15, 21]

resultado2 = valores_multiplicados_segundo([1])
print(resultado2)  #Imprime 1 y devolverá []

#Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud. 
# La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida
# y los valores sean igual a la longitud multiplicada por el valor dado.
#Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
#Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]
def valor_multiplicado_longitud(valor, longitud):
    return [valor * longitud] * longitud
resultado1 = valor_multiplicado_longitud(5, 2)
print(resultado1)  #Imprime [10, 10]

resultado2 = valor_multiplicado_longitud(7, 5)
print(resultado2)  # Imprime [35, 35, 35, 35, 35]
