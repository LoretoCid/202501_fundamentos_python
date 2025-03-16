from TarjetaCredito import TarjetaCredito

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta = TarjetaCredito(0, 20000, 0.015) #Agregamos esta línea
        self.saldo_pagar = 0
    
    def hacer_compra(self, monto):
        self.tarjeta.compra(monto)  #llama al método compra de la clase TarjetaCredito
    
    def pagar_tarjeta(self, monto):
        self.tarjeta.pago(monto)
    
    def mostrar_saldo_usuario(self):    
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.tarjeta.saldo_pagar}")    #muestra el saldo a pagar del usuario

#BONUS
#permite que un usuario tenga varias tarjetas de crédito. 
#Actualiza los métodos para que el usuario pueda especificar en qué cuenta está realizando una compra o a qué tarjeta está pagando.
from TarjetaCredito import TarjetaCredito

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = [] #Muchas tarjetas

    def agregar_tarjeta(self, limite_credito, intereses):
        tarjeta = TarjetaCredito(limite_credito, intereses)
        self.tarjetas.append(tarjeta)
    
    def hacer_compra(self, monto, indice_tarjeta):
        if 0 <= indice_tarjeta < len(self.tarjetas):
            self.tarjetas[indice_tarjeta].compra(monto)
        else:
            print("Índice de tarjeta no válido")
    
    def pagar_tarjeta(self, monto, indice_tarjeta):
        if 0 <= indice_tarjeta < len(self.tarjetas):
            self.tarjetas[indice_tarjeta].pago(monto)
        else:
            print("Índice de tarjeta no válido")
    
    def mostrar_saldo_usuario(self):    
        for i, tarjeta in enumerate(self.tarjetas):
            print(f"Tarjeta {i + 1}: Saldo a Pagar: ${tarjeta.saldo_pagar}")

#
usuario = Usuario("Loreto", "Cid", "lore.cid921@gmail.com")
usuario.agregar_tarjeta(20000, 0.015)
usuario.agregar_tarjeta(15000, 0.02)

usuario.hacer_compra(5000, 0)  # Realiza una compra en la primera tarjeta
usuario.pagar_tarjeta(2000, 1)  # Realiza un pago en la segunda tarjeta

usuario.mostrar_saldo_usuario()
