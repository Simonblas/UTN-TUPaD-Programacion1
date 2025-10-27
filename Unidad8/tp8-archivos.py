# 1)Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad
def sobreescribirProductos():
    with open("./productos.txt", "w") as productos:
        listaProductosInicial = [
            "escoba,20,100\n",
            "pala,30,110\n",
            "lavandina,40,51\n",
        ]
        productos.writelines(listaProductosInicial)


# # 2)Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30
def leerProductos():
    with open("./productos.txt", "r") as productos:
        lineas = productos.readlines()
        for linea in lineas:
            partes = linea.strip().split(",")
            print(f"{partes[0]} | precio: ${partes[1]} | Cantidad: {partes[2]}")


# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.
def agregarProductos():
    leerProductos()
    nombreProductoNuevo = input("Ingrese el nombre del producto: ")
    precioProductoNuevo = input("Ingrese el precio del producto: ")
    cantidadProductoNuevo = input("Ingrese la cantidad del producto: ")
    with open("./productos.txt", "a") as productos:
        productos.write(
            f"{nombreProductoNuevo},{precioProductoNuevo},{cantidadProductoNuevo}\n"
        )


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.
def cargarProductos():
    productos = []
    with open("./productos.txt", "r") as archivoProductos:
        lineas = archivoProductos.readlines()
        for linea in lineas:
            partes = linea.strip().split(",")
            if len(partes) == 3:
                elemento = {
                    "nombre": partes[0],
                    "precio": float(partes[1]),
                    "cantidad": int(partes[2]),
                }
                productos.append(elemento)
    return productos


# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.
def buscarProductoPorNombre():
    nombreProducto = input("Ingrese el nombre del producto a buscar: ")
    productos = cargarProductos()
    productoEncontrado = None
    for producto in productos:
        if producto["nombre"].lower() == nombreProducto.lower():
            productoEncontrado = producto
            break
    if productoEncontrado:
        print(
            f'El producto: {productoEncontrado["nombre"]} tiene un precio de: {productoEncontrado["precio"]} y una cantidad de: {productoEncontrado["cantidad"]}'
        )
    else:
        print("El producto no pudo ser encontrado.")


# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.


def actualizarProductos(lista):
    with open("productos.txt", "w") as productos:
        partes = []
        for elemento in lista:
            partes.append(
                f'{elemento["nombre"]},{elemento["precio"]},{elemento["cantidad"]}\n'
            )
        productos.writelines(partes)
    print("archivo actualizado correctamente.")


def menuProductos():
    opcion = 0
    print(
        "Menu:\n1) leer productos\n2) agregar productos\n3) buscar producto por nombre\n4) actualizar productos\n5) salir"
    )
    while opcion != 5:
        productos = cargarProductos()
        opcion = int(input("Ingrese una opcion (1 | 2 | 3 | 4 | 5): "))
        match opcion:
            case 1:
                leerProductos()
            case 2:
                agregarProductos()
            case 3:
                buscarProductoPorNombre()
            case 4:
                actualizarProductos(productos)
            case 5:
                opcion = 5


menuProductos()
