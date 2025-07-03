from base_de_datos import login
import cliente
import insumos
import proveedor
import maquina
import mantenimiento
import tecnicos
from registro_consumo import calcular_costo_insumos_mensual

def mostrar_menu(es_admin):
    print("1. Agregar cliente")
    print("2. Eliminar cliente")
    print("3. Modificar cliente")
    print("4. Agregar insumo")
    print("5. Eliminar insumo")
    print("6. Ver reporte de costos mensuales")

    if es_admin:
        print("7. Agregar proveedor")
        print("8. Eliminar proveedor")
        print("9. Agregar técnico")
        print("10. Eliminar técnico")
        print("11. Agregar máquina")
        print("12. Eliminar máquina")
        print("13. Agregar mantenimiento")
        print("14. Eliminar mantenimiento")

        print("15. Modificar insumo")
        print("16. Modificar proveedor")
        print("17. Modificar técnico")
        print("18. Modificar máquina")
        print("19. Modificar mantenimiento")





    print("0. Salir")

def main():
    correo = input("Correo: ")
    contrasena = input("Contraseña: ")
    usuario = login(correo, contrasena)

    if not usuario:
        print("Credenciales inválidas.")
        return

    es_admin = usuario[1]
    print(f"\n Bienvenido {correo} {'(ADMIN)' if es_admin else ''}")

    while True:
        mostrar_menu(es_admin)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            correo = input("Correo electrónico: ")
            print(cliente.agregar_cliente(nombre, direccion, telefono, correo))

        elif opcion == "2":
            id = input("ID del cliente a eliminar: ")
            print(cliente.eliminar_cliente(id))

        elif opcion == "3":
            id = input("ID del cliente: ")
            nombre = input("Nuevo nombre: ")
            direccion = input("Nueva dirección: ")
            telefono = input("Nuevo teléfono: ")
            correo = input("Nuevo correo: ")
            print(cliente.modificar_cliente(id, nombre, direccion, telefono, correo))

        elif opcion == "4":
            descripcion = input("Descripción del insumo: ")
            tipo = input("Tipo: ")
            precio = int(input("Precio unitario: "))
            id_proveedor = input("ID proveedor: ")
            print(insumos.agregar_insumo(descripcion, tipo, precio, id_proveedor))

        elif opcion == "5":
            id = input("ID del insumo a eliminar: ")
            print(insumos.eliminar_insumo(id))

        elif opcion == "6":
            mes = input("Mes (1-12): ")
            anio = input("Año (YYYY): ")
            print(calcular_costo_insumos_mensual(mes, anio))

        elif es_admin and opcion == "7":
            nombre = input("Nombre proveedor: ")
            contacto = input("Contacto: ")
            print(proveedor.agregar_proveedor(nombre, contacto, usuario))

        elif es_admin and opcion == "8":
            id = input("ID proveedor: ")
            print(proveedor.eliminar_proveedor(id, usuario))

        elif es_admin and opcion == "9":
            ci = input("Cédula: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            print(tecnicos.agregar_tecnico(ci, nombre, apellido, telefono, usuario))

        elif es_admin and opcion == "10":
            ci = input("Cédula técnico a eliminar: ")
            print(tecnicos.eliminar_tecnico(ci, usuario))

        elif es_admin and opcion == "11":
            modelo = input("Modelo: ")
            id_cliente = input("ID cliente: ")
            ubicacion = input("Ubicación: ")
            costo = int(input("Costo alquiler mensual: "))
            print(maquina.agregar_maquina(modelo, id_cliente, ubicacion, costo, usuario))

        elif es_admin and opcion == "12":
            id = input("ID máquina: ")
            print(maquina.eliminar_maquina(id, usuario))

        elif es_admin and opcion == "13":
            id_maquina = input("ID máquina: ")
            ci_tecnico = input("CI técnico: ")
            tipo = input("Tipo mantenimiento: ")
            fecha = input("Fecha (YYYY-MM-DD HH:MM:SS): ")
            observaciones = input("Observaciones: ")
            print(mantenimiento.agregar_mantenimiento(id_maquina, ci_tecnico, tipo, fecha, observaciones))

        elif es_admin and opcion == "14":
            id = input("ID mantenimiento: ")
            print(mantenimiento.eliminar_mantenimiento(id))

        elif es_admin and opcion == "15":
            id = input("ID del insumo a modificar: ")
            descripcion = input("Nueva descripción: ")
            tipo = input("Nuevo tipo: ")
            precio = int(input("Nuevo precio unitario: "))
            id_prov = input("Nuevo ID de proveedor: ")
            print(insumos.modificar_insumo(id, descripcion, tipo, precio, id_prov))

        elif es_admin and opcion == "16":
            id = input("ID del proveedor a modificar: ")
            nombre = input("Nuevo nombre: ")
            contacto = input("Nuevo contacto: ")
            print(proveedor.modificar_proveedor(id, nombre, contacto, usuario))

        elif es_admin and opcion == "17":
            ci = input("Cédula del técnico: ")
            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo apellido: ")
            telefono = input("Nuevo teléfono: ")
            print(tecnicos.modificar_tecnico(ci, nombre, apellido, telefono, usuario))

        elif es_admin and opcion == "18":
            id = input("ID de la máquina: ")
            modelo = input("Nuevo modelo: ")
            id_cliente = input("Nuevo ID de cliente: ")
            ubicacion = input("Nueva ubicación: ")
            costo = int(input("Nuevo costo mensual: "))
            print(maquina.modificar_maquina(id, modelo, id_cliente, ubicacion, costo, usuario))

        elif es_admin and opcion == "19":
            id = input("ID del mantenimiento a modificar: ")
            id_maquina = input("Nuevo ID de máquina: ")
            ci_tecnico = input("Nueva cédula de técnico: ")
            tipo = input("Nuevo tipo de mantenimiento: ")
            fecha = input("Nueva fecha (YYYY-MM-DD HH:MM:SS): ")
            observaciones = input("Nuevas observaciones: ")
            print(mantenimiento.modificar_mantenimiento(id, id_maquina, ci_tecnico, tipo, fecha, observaciones))

        elif opcion == "0":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
