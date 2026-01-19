from agenda import Agenda
from contacto import Contacto

def mostrar_menu():
    print("\n=== AGENDA DE CONTACTOS ===")
    print("1. Agregar contacto")
    print("2. Buscar contacto por teléfono")
    print("3. Buscar contacto por nombre")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Listar contactos")
    print("0. Salir")


agenda = Agenda()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1": # Añadir
        try:
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")

            contacto = Contacto(nombre, telefono, correo, direccion) #Validaciones
            if agenda.agregar_contacto(contacto):
                print("Contacto agregado correctamente")
            else:
                print("Ya existe un contacto con ese teléfono")
        except ValueError as error: # Uso de Try - catch para manejo de errores
            print(f"Error: {error}")


    elif opcion == "2": #buscar por telefono
        telefono = input("Ingrese teléfono a buscar: ")
        contacto = agenda.buscar_por_telefono(telefono)

        if contacto:
            print("Nombre:", contacto.obtener_nombre())
            print("Teléfono:", contacto.obtener_telefono())
        else:
            print("Contacto no encontrado")

    elif opcion == "3": #buscar por nombre
        nombre = input("Ingrese nombre a buscar: ")
        resultados = agenda.buscar_por_nombre(nombre)

        if resultados:
            for c in resultados:
               print(
                   "RESULTADOS - Nombre:", c.obtener_nombre(),
                   "Teléfono:", c.obtener_telefono())
        else:
            print("No se encontraron contactos")

    elif opcion == "4": #editar contacto
        telefono = input("Teléfono del contacto a editar: ")
        nuevo_nombre = input("Nuevo nombre (enter para no cambiar): ")
        nuevo_correo = input("Nuevo correo (enter para no cambiar): ")
        nueva_direccion = input("Nueva dirección (enter para no cambiar): ")

        if agenda.editar_contacto(
            telefono,
            nuevo_nombre if nuevo_nombre else None,
            nuevo_correo if nuevo_correo else None,
            nueva_direccion if nueva_direccion else None
        ):
            print("Contacto editado")
        else:
            print("Contacto no encontrado")

    elif opcion == "5": #eliminar contacto
        telefono = input("Teléfono del contacto a eliminar: ")
        if agenda.eliminar_contacto(telefono):
            print("🗑️ Contacto eliminado")
        else:
            print("Contacto no encontrado")

    elif opcion == "6": #listar contactos
        contactos = agenda.listar_contactos()
        if not contactos:
            print("Agenda vacía")
        else:
            for c in contactos:
                print("-", c.obtener_nombre(), c.obtener_telefono())

    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida")
