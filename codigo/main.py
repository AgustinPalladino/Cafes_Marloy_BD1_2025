import mantenimiento
import tecnicos
import proveedor
import base_de_datos
import maquina
import insumos
import cliente

user = base_de_datos.login("admin@cafesmarloy.com","admin123")


cliente.eliminar_cliente(1)
insumos.eliminar_insumo(1)
mantenimiento.eliminar_mantenimiento(1)
maquina.eliminar_maquina(1, user)
proveedor.eliminar_proveedor(1, user)
tecnicos.eliminar_tecnico("12", user)