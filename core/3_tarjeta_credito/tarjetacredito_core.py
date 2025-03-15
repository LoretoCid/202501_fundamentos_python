class TarjetaCredito:
    #Incluye en este método valores por default
    tarjetas = []
    
    def __init__(self, saldo_pagar, limite_credito, intereses):
        self.saldo_pagar = saldo_pagar
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

#Crea 3 tarjetas
tarjeta1 = TarjetaCredito(saldo_pagar=0, limite_credito=5000, intereses=0.03)
tarjeta2 = TarjetaCredito(saldo_pagar=1000, limite_credito=3000, intereses=0.05)
tarjeta3 = TarjetaCredito(saldo_pagar=3000, limite_credito=10000, intereses=0.04)

#Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta;
# todo esto en una sola línea a través de la encadenación.
tarjeta1.compra(500); tarjeta1.compra(1000); tarjeta1.pago(300); tarjeta1.cobrar_interes(); tarjeta1.mostrar_info_tarjeta() #saldo a pagar de 1236.0

#Para la segunda tarjeta, haz 3 compras y 2 pagos.
#Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
tarjeta2.compra(200); tarjeta2.compra(500); tarjeta2.compra(1000); tarjeta2.pago(1000); tarjeta2.pago(500); tarjeta2.cobrar_interes(); tarjeta2.mostrar_info_tarjeta() 

#Para la tercera tarjeta, haz 5 compras y excede su límite de crédito.
#Luego muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
tarjeta3.compra(2000); tarjeta3.compra(3000); tarjeta3.compra(2000); tarjeta3.compra(2000); tarjeta3.compra(2000); tarjeta3.mostrar_info_tarjeta() 

#BONUS: crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas.
# En el capítulo pasado te dimos algunas pistas de cómo realizarlo.
TarjetaCredito.mostrar_todas_las_tarjetas()