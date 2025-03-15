class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto   #el saldo a pagar del usuario disminuye en la cantidad del valor recibido
    
    def mostrar_saldo(self):
        return self.saldo_pagar
    
    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")    #muestra el saldo a pagar del usuario   
    
    def transferir_deuda(self, otro_usuario, monto):
        if monto <= 0:
            print("El monto debe ser positivo.")
        elif monto > self.saldo_pagar:
            print(f"No puedes transferir más de lo que debes. Tu saldo a pagar es ${self.saldo_pagar}.")
        else:
            self.saldo_pagar -= monto
            otro_usuario.saldo_pagar += monto
            print(f"Se han transferido ${monto} de deuda a {otro_usuario.nombre} {otro_usuario.apellido}.")   #transfiere la deuda de un usuario a otro

# Crear tres instancias de la clase Usuario
usuario1 = Usuario("Loreto", "Cid", "lore.cid921@gmail.com")
usuario2 = Usuario("Macarena", "Olguin", "maca.olguin@gmail.com")
usuario3 = Usuario("Fernanda", "Cuevas", "fer.cuevas@gmsil.com")

# Haz que el primer usuario haga 2 compras y luego pague su tarjeta. Muestra su saldo
# usuario1 realiza dos compras
usuario1.hacer_compra(5000)  # Compra de 5000
print(f"Después de la primera compra de 5000, el saldo a pagar es: ${usuario1.mostrar_saldo()}")
usuario1.hacer_compra(12000)  # Compra de 12000
print(f"Después de la segunda compra de 12000, el saldo a pagar es: ${usuario1.mostrar_saldo()}")
# El primer usuario paga una parte de su saldo
usuario1.pagar_tarjeta(7000)  # Paga 7000
print(f"Después de pagar 7000, el saldo a pagar es: ${usuario1.mostrar_saldo()}")
# Mostrar el saldo final del primer usuario
usuario1.mostrar_saldo_usuario()

#Haz que el segundo usuario haga 1 compra y luego pague 2 veces su tarjeta. Muestra su saldo
usuario2.hacer_compra(10000)  # Compra de 10000
print(f"Después de la compra de 10000, el saldo a pagar es: ${usuario2.mostrar_saldo()}")
usuario2.pagar_tarjeta(2000)  # Paga 2000
usuario2.pagar_tarjeta(3000)  # Paga 3000
usuario2.mostrar_saldo_usuario()

#Haz que el tercer usuario haga 3 compras y luego pague su tarjeta 4 veces. Muestra su saldo
usuario3.hacer_compra(1000)  # Compra de 1000
usuario3.hacer_compra(2000)  # Compra de 2000
usuario3.hacer_compra(3000)  # Compra de 3000
usuario3.pagar_tarjeta(500)  # Paga 500
usuario3.pagar_tarjeta(600)  # Paga 600
usuario3.pagar_tarjeta(700)  # Paga 700
usuario3.pagar_tarjeta(800)  # Paga 800
usuario3.mostrar_saldo_usuario()