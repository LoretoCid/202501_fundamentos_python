class TarjetaCredito:
    #Incluye en este método valores por default
    tarjetas = []
    
    def __init__(self, limite_credito, intereses):
        self.saldo_pagar = 0
        self.limite_credito = limite_credito
        self.intereses = intereses

        TarjetaCredito.tarjetas.append(self)

    def compra(self, monto): 
    #aumenta el saldo_pagar de acuerdo al monto recibido siempre y cuando la tarjeta de crédito no haya llegado a su límite crediticio. 
    # De lo contrario, que imprima: “Tarjeta Rechazada, has alcanzado tu límite de crédito”.
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto  # Aumentamos el saldo a pagar con el monto de la compra
            print(f"Compra realizada de {monto}. Nuevo saldo a pagar: {self.saldo_pagar}")
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito.")

    def pago(self, monto): #disminuye el saldo_pagar de la tarjeta.
        self.saldo_pagar -= monto
        print(f"Pago realizado de {monto}. Nuevo saldo a pagar: {self.saldo_pagar}") 

    def mostrar_info_tarjeta(self): #imprime en la consola el saldo a pagar de la tarjeta.
        print(f"Saldo a pagar: {self.saldo_pagar}")
    
    def cobrar_interes(self): #aumenta el saldo_pagar cobrando intereses. Es decir al saldo_pagar actual se le agregará el saldo_pagar * los intereses.
        self.saldo_pagar += self.saldo_pagar * self.intereses
        print(f"Intereses cobrados. Nuevo saldo a pagar: {self.saldo_pagar}")
    
    @classmethod
    def mostrar_todas_las_tarjetas(cls): #método de clase que imprime todas las instancias de la información de las tarjetas creadas.
        for tarjeta in cls.tarjetas:
            print(f"Saldo a pagar: {tarjeta.saldo_pagar}, Límite de crédito: {tarjeta.limite_credito}, Intereses: {tarjeta.intereses}")
            tarjeta.mostrar_info_tarjeta()
