from Lista import ListaEnlazada
from tkinter.filedialog import askopenfilename
from xml.etree import ElementTree as ET

telefono = ListaEnlazada()

if __name__=='__main__':
    print("Bienvenido")
    print("""Desea cargar los contactos de ¿?: 
            1. Forma manual
            2. Por archivo""")
    des = int(input("Ingrese una opción (número): "))
    print("")
    if des == 1:
        can = int(input("¿Cuántos números desea agregar?:"))
        for i in range(can):
            tel = (input("Ingrese el teléfono: "))
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido")
            telefono.insertar(tel, nombre)
    elif des == 2:
        ruta = askopenfilename(title="Seleccione un archivo")
        arb = ET.parse(ruta)
        raiz = arb.getroot()
        tel_xml = nom_xml = ape_xml = ""
        for elem in raiz:
            for subelem in elem:
                if subelem.tag == "telefono":
                    tel_xml = subelem.text
                elif subelem.tag == "nombre":
                    nom_xml = subelem.text
                elif subelem.tag == "apellido":
                    ape_xml = subelem.text
            telefono.insertar(tel_xml, nom_xml,ape_xml)
    else:
        print("No seleccionó una opción válida")

    print("A continuación se mostrarán los teléfonos\n")
    telefono.mostrar()