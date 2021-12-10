from Lista import ListaEnlazada

telefono = ListaEnlazada()

if __name__=='__main__':
    print("Bienvenido")
    can = int(input("¿Cuántos números desea agregar?:"))
    for i in range(can):
        tel = (input("Ingrese el teléfono: "))
        nombre = input("Ingrese el nombre: ")
        telefono.insertar(tel, nombre)

    print("A continuación se mostrarán los teléfonos")
    telefono.mostrar()