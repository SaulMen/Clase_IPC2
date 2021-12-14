from Datos import Datos

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar(self, tel, nom, ape):
        new = Datos(tel, nom, ape)
        bandera = True
        if self.inicio == None:
            self.inicio = new
        else:
            temp = self.inicio
            while temp != None:
                if temp.tel == new.tel:
                    #print(temp.tel, new.tel, "iguales")
                    bandera = False
                temp = temp.next

            temp = self.inicio
            if bandera:
                while temp.next != None:
                    temp = temp.next
                temp.next = new
            else:
                print(f"Error, se omitió este contacto ({new.tel})")
                print("Porque ya existe en nuestra agenda.\n")

    def ordenar(self):
        temp = self.inicio
        while temp.next != None:
            temp = temp.next

    def mostrar(self):
        temp = self.inicio
        cont = 1
        while temp is not None:
            print(f"{cont}.)", end=" ")
            print(f"Apellido: {temp.ape}", end=", ")
            print(f"Nombre {temp.nom}", end=", ")
            print(f"Telefono {temp.tel}")
            temp = temp.next
            cont += 1
    
    def ordenar(self):
        temp = self.inicio
        cont = 1
        while temp is not None:
            temp = temp.next
            cont += 1
        
        while cont != 0:
            if ord(temp.ape[0]) > ord(temp.ape[0]):
                pass
            cont +=1

            

        
                
        
