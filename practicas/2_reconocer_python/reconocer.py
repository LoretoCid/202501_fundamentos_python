# Asignación de valores a variables
numero1 = 70  # Variable de tipo entero
numero2 = 3.14 # Variable de tipo flotante
booleano = False # Variable booleana con valor False
cadena = 'Hola Mundo' # Variable de tipo string o cadena
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] # Lista
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False}  # Diccionario
frutas = ('guayaba', 'fresa', 'papaya') # Tupla con frutas
print(type(frutas)) # Muestra el tipo de dato de la variable 'frutas' (Tupla)
print(ingredientes_pastel[2]) # Imprime el tercer elemento de la lista de ingredientes (índice 2)
ingredientes_pastel.append('Mantequilla') # Añade un nuevo ingrediente a la lista de ingredientes
print(persona['nombre']) # Muestra el nombre de la persona usando el diccionario

# Cambia el valor de 'nombre' en el diccionario y añade un nuevo campo 'color_ojos'
persona['nombre'] = 'Kevin' 
persona['color_ojos'] = 'cafe' 
print(frutas[2]) # Imprime el tercer elemento de la tupla 'frutas' (índice 2)

# Condicional para verificar si el número es mayor a 45
if numero1 > 45:
    print("Numero mayor")
else:
    print("Numero menor")

# Verifica la longitud de la cadena e imprime un mensaje 
if len(cadena) < 5:
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")

for x in range(8): # Ciclo 'for' para imprimir los números del 0 al 7
    print(x)
for x in range(2,8): # Ciclo 'for' para imprimir los números del 2 al 7
    print(x)
for x in range(2,8,2): # Ciclo 'for' para imprimir los números del 2 al 7, de 2 en 2
    print(x)
x = 0 # Ciclo 'while' para imprimir números del 0 al 7
while(x < 8):
    print(x)
    x += 1

ingredientes_pastel.pop() # Eliminar el último ingrediente de la lista
ingredientes_pastel.pop(1) # Eliminar el segundo ingrediente de la lista (índice 1)
print(persona) # Imprime el diccionario 'persona'
persona.pop('color_ojos') # Elimina 'color_ojos' del diccionario 'persona'
print(persona) # Elimina el campo 'color_ojos' del diccionario 'persona'

# Ciclo 'for' para recorrer la lista de ingredientes
for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':   # Si el ingrediente es 'Harina', se salta esta iteración del ciclo
        continue
    print('Después de la primera sentencia')  # Imprime un mensaje después de la sentencia 'continue'
    if ingrediente == 'Chocolate':
        break    # Si el ingrediente es 'Chocolate', se detiene el ciclo

def imprime_hola_10_veces(): # Definición de una función que imprime 'Hola' 10 veces
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces() # Llama a la función para imprimir 'Hola' 10 veces

def imprime_hola_n_veces(n): # Función que imprime 'Hola' 'n' veces, donde 'n' es un parámetro
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5) # Llama a la función para imprimir 'Hola' 5 veces

def imprime_hola_n_o_diez_veces(n = 10): # Función con un valor predeterminado para el parámetro 'n' (10 veces si no se pasa un valor)
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces() # Llama a la función para imprimir 'Hola' 10 veces (valor predeterminado de 'n')
imprime_hola_n_o_diez_veces(5) # Llama a la función para imprimir 'Hola' 5 veces (se pasa un valor para 'n')


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)