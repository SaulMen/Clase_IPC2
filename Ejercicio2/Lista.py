from Datos import Datos

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar(self, tel, nom):
        new = Datos(tel, nom)

        if self.inicio == None:
            self.inicio = new
        else:
            temp = self.inicio
            while temp.next is not None:
                temp = temp.next
            temp.next = new
    
    def mostrar(self):
        temp = self.inicio
        cont = 1
        while temp is not None:
            print(f"{cont}.)", end=" ")
            print(f"Telefono: {temp.tel}", end=", ")
            print(f"Nombre {temp.nom}")
            temp = temp.next
            cont += 1
        
                
        
