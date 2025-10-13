# 1) Dado el diccionario precios_frutas
precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
frutas_sin_precios = list(precios_frutas.keys())

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
diccionario_contactos = dict()

for i in range(0, 5):
    nombre_contacto = input("Ingrese el nombre del contacto: ")
    numero_telefono = input("Ingrese el numero de telefono del contacto: ")
    diccionario_contactos[nombre_contacto] = numero_telefono
buscar_contacto = input("Ingrese el nombre de un contacto a buscar: ")
if buscar_contacto in diccionario_contactos:
    print("El numero del contacto buscado es: ", diccionario_contactos[buscar_contacto])
else:
    print("El contacto buscado no pudo ser encontrado.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
frase_usuario = input("Ingrese una frase: ")
palabras = frase_usuario.split()
palabras_unicas = set(palabras)
cantidad_palabras = {}
for palabra in palabras:
    cantidad_palabras[palabra] = cantidad_palabras.get(palabra, 0) + 1
print(f"Las palabras unicas son: {palabras_unicas}")
print(f"Recuento: {cantidad_palabras}")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
alumnos = {}
alumno = ""
for i in range(3):
    notas = []
    alumno = input("Ingrese el nombre del alumno: ")
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {alumno}: "))
        notas.append(nota)
    alumnos[alumno] = tuple(notas)
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} tiene un promedio de: {round(promedio,2)}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
aprobados_parcial1 = {1, 2, 3, 4}
aprobados_parcial2 = {2, 4, 5, 8, 9}
print(
    f"Estudiantes que aprobaron ambos parciales: {aprobados_parcial1 & aprobados_parcial2}"
)
print(
    f"Estudiantes que aprobaron solo un parcial: {aprobados_parcial1 ^ aprobados_parcial2}"
)
print(
    f"Estudiantes que aprobaron al menos un parcial: {aprobados_parcial1 | aprobados_parcial2}"
)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
mercaderia = {}
bandera = True


def consultarStock(producto):
    if producto in mercaderia:
        print(f"{producto} Tiene un total de: {mercaderia[producto]} unidad/es")
    else:
        print("El producto aun no se registro")


def agregarUnidades(producto: str, agregado: int):
    if producto in mercaderia:
        mercaderia[producto] += agregado
    else:
        print("El producto aun no esta registrado.")


def agregarProducto(producto: str, stock: int):
    if not producto in mercaderia:
        mercaderia[producto] = stock
    else:
        print("El producto ya esta registrado.")


while bandera == True:
    print(
        "Opciones:\n"
        "1: Consultar Stock\n"
        "2: Agregar Unidades\n"
        "3: Agregar Producto\n"
        "4: Salir"
    )
    opcion = input("Ingrese la opcion: ")
    match opcion:
        case "1":
            producto1 = input("Ingrese el nombre del producto: ")
            consultarStock(producto1)
        case "2":
            producto2 = input("Ingrese el nombre del producto: ")
            agregado = int(input("Ingrese la cantidad a agregar: "))
            agregarUnidades(producto2, agregado)
        case "3":
            producto3 = input("Ingrese el nombre del producto: ")
            stock = int(input("Ingrese la cantidad del stock: "))
            agregarProducto(producto3, stock)
        case "4":
            bandera = False
            print("Saliendo del programa.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.
agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de Ingles",
}


def consultarActividad(dia, hora):
    if (dia, hora) in agenda:
        print("Actividad: ", agenda[(dia, hora)])


dia = input("Ingrese el dia: ")
hora = input("Ingrese la hora (hora:minuto): ")
consultarActividad(dia, hora)

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
}
invertido = {}
for key, value in original.items():
    invertido[value] = key
print(f"El diccionario invertido es: {invertido}")
