from Datos import Datos
from os import system,startfile

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
    
    def reporte(self):
        cabecera = self.inicio
        temp = self.inicio
        cont = 1
        grafo = """
                digraph G {
                node[shape=box fillcolor="#FFEDBB", style=filled]
                label = "Contactos"
                bgcolor = "#398D9C"
                    subgraph G {
                        edge[dir="both"]
                """    
        
        while temp is not None:
            grafo+=f'q{cont}[label="{temp.nom} {temp.ape} {temp.tel}"]'
            temp = temp.next
            cont += 1
        temp = self.inicio
        cont = 1
        while temp.next != None:
            grafo+='{rankdir = "TB";'
            grafo+=f'q{cont}->q{cont+1}'
            grafo+='}\n'
            cont += 1
            temp = temp.next

        grafo+="""
                }
                    }
            """
        arhivo_grafo = open('contactos.dot','w')
        arhivo_grafo.write(grafo)
        arhivo_grafo.close()

        system("dot -Tpng contactos.dot -o contactos.png")
        startfile("contactos.png")

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

            

        
                
        
