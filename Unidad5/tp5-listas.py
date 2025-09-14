# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.
notas_estudiantes = [9.00, 8.75, 5.75, 10, 8.00, 7.25, 6.00, 4.25, 2.00, 1]
promedio = 0
nota_mas_baja = 99
nota_mas_alta = -1

for nota in notas_estudiantes:
    print(nota)
    promedio += nota
    if nota > nota_mas_alta:
        nota_mas_alta = nota
    if nota < nota_mas_baja:
        nota_mas_baja = nota
promedio = promedio / len(notas_estudiantes)
print(f"el promedio de notas es: {promedio}")
print(f"La nota mas alta es: {nota_mas_alta} y la nota mas baja es: {nota_mas_baja}")

# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
lista_productos = []

for i in range(0, 5):
    producto = input("Ingrese un producto: ")
    lista_productos.append(producto)

print(f"La lista de productos quedo de esta manera: {lista_productos}")
print(
    f"La lista ordenada alfabeticamente quedo de esta manera: {sorted(lista_productos)}"
)

lista_productos.remove(input("Ingresa el nombre producto que deseas eliminar: "))
print(f"La lista actualizada es: {lista_productos}")

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.
import random

lista_numeros_azar = []
lista_azar_pares = []
lista_azar_impares = []

lista_numeros_azar = list(random.randint(1, 100) for i in range(15))
print(f"La lista inicial es: {lista_numeros_azar}")

for i in range(0, len(lista_numeros_azar)):
    if lista_numeros_azar[i] % 2 == 0:
        lista_azar_pares.append(lista_numeros_azar[i])
    else:
        lista_azar_impares.append(lista_numeros_azar[i])

print(
    f"La lista de pares tiene {len(lista_azar_pares)} numeros y es: {lista_azar_pares}"
)
print(
    f"La lista de impares tiene {len(lista_azar_impares)} numeros y es: {lista_azar_impares}"
)


# 4) Dada una lista con valores repetidos:
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
print(f"La lista inicial es: {datos}")
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.
lista_sin_repetidos = []
for item in datos:
    if item not in lista_sin_repetidos:
        lista_sin_repetidos.append(item)
print(
    f"La lista sin repetidos y manteniendo orden de lectura es: {lista_sin_repetidos}"
)


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.
estudiantes_en_clase = [
    "Simon",
    "Lautaro",
    "Camilo",
    "Brisa",
    "Juana",
    "Guadalupe",
    "Franco",
    "Teo",
]
editar_lista_estudiantes = ""
print(f"La lista inicial de estudiantes es: {estudiantes_en_clase}")
editar_lista_estudiantes = input(
    "Quieres agregar o eliminar algun estudiante? (agregar/eliminar): "
)
if editar_lista_estudiantes.lower() == "agregar":
    estudiantes_en_clase.append(input("Indique el nombre del estudiante a agregar: "))
elif editar_lista_estudiantes.lower() == "eliminar":
    estudiantes_en_clase.remove(input("Indique el nombre del estudiante a eliminar: "))
else:
    print("Respuesta incorrecta, debe ser 'Eliminar' o 'Agregar.'")

print(f"La lista final de estudiantes es: {estudiantes_en_clase}")

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

lista_siete = [1, 2, 3, 4, 5, 6, 7]
print(f"Lista inicial de 7 numeros: {lista_siete}")
lista_siete.insert(0, lista_siete[len(lista_siete) - 1])
lista_siete.pop(len(lista_siete) - 1)
print(f"Lista final de 7 numeros: {lista_siete}")

# otra forma con bucle for:
lista_siete_inicial = [1, 2, 3, 4, 5, 6, 7]
lista_siete_final = []
print(f"Lista inicial de 7 numeros: {lista_siete_inicial}")
for i in range(0, len(lista_siete_inicial)):
    lista_siete_final.append(lista_siete_inicial[i - 1])
print(f"Lista final de 7 numeros: {lista_siete_final}")


# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

matriz_semanal_temperaturas = [
    [5, 23],
    [2, 15],
    [-2, 10],
    [3, 14],
    [8, 25],
    [12, 30],
    [20, 34],
]
promedio_minimas = 0
promedio_maximas = 0
dia_mayor_amplitud = 0
mayor_amplitud = 0
print("Matriz semanal de temperaturas: ")
for i in range(len(matriz_semanal_temperaturas)):
    print(f"Para el dia {i+1} : {matriz_semanal_temperaturas[i]}")


for i in range(0, len(matriz_semanal_temperaturas)):
    promedio_minimas += matriz_semanal_temperaturas[i][0]
    promedio_maximas += matriz_semanal_temperaturas[i][1]
    if (
        matriz_semanal_temperaturas[i][1] - matriz_semanal_temperaturas[i][0]
        > mayor_amplitud
    ):
        mayor_amplitud = (
            matriz_semanal_temperaturas[i][1] - matriz_semanal_temperaturas[i][0]
        )
        dia_mayor_amplitud = i
promedio_minimas = promedio_minimas // len(matriz_semanal_temperaturas)
promedio_maximas = promedio_maximas // len(matriz_semanal_temperaturas)
print(f"El promedio de las temperaturas minimas es: {promedio_minimas}")
print(f"El promedio de las temperaturas maximas es: {promedio_maximas}")
print(
    f"El dia con mayor amplitud fue el numero: {dia_mayor_amplitud+1}, con una diferencia de temperaturas de: {mayor_amplitud}° entre la minima y maxima"
)


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.
matriz_notas_estudiante_materia = [
    [6, 7, 8],
    [6, 5, 4],
    [10, 9, 8],
    [10, 7, 3],
    [7, 7, 7],
]
promedio_estudiante = 0
promedio_materia1 = 0
promedio_materia2 = 0
promedio_materia3 = 0

for i in range(0, len(matriz_notas_estudiante_materia)):
    for j in range(0, len(matriz_notas_estudiante_materia[0])):
        promedio_estudiante += matriz_notas_estudiante_materia[i][j]
    promedio_estudiante = round(
        promedio_estudiante / len(matriz_notas_estudiante_materia[0]), 2
    )
    print(f"La nota promedio del estudiante numero {i+1} es: {promedio_estudiante}")
    promedio_estudiante = 0
    promedio_materia1 += matriz_notas_estudiante_materia[i][0]
    promedio_materia2 += matriz_notas_estudiante_materia[i][1]
    promedio_materia3 += matriz_notas_estudiante_materia[i][2]

promedio_materia1 = round(promedio_materia1 / len(matriz_notas_estudiante_materia), 2)
promedio_materia2 = round(promedio_materia2 / len(matriz_notas_estudiante_materia), 2)
promedio_materia3 = round(promedio_materia3 / len(matriz_notas_estudiante_materia), 2)
print(
    f"""El promedio de cada materia es:
Materia 1: {promedio_materia1}
Materia 2: {promedio_materia2}
Materia 3: {promedio_materia3}
"""
)

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

matriz_tateti = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
seguirJugando = "s"
posicion1 = -1
posicion2 = -1
simbolo = ""
for i in range(0, len(matriz_tateti)):
    print(matriz_tateti[i])

while seguirJugando.lower() == "s":
    posicion1 = int(input("Ingrese la fila (1-3): ")) - 1
    posicion2 = int(input("Ingrese la columna (1-3): ")) - 1
    simbolo = input("Ingrese 'X' o 'O': ")
    if (
        (0 <= posicion1 <= 2)
        and (0 <= posicion2 <= 2)
        and (simbolo.lower() == "x" or simbolo.lower() == "o")
    ):
        matriz_tateti[posicion1][posicion2] = simbolo
    else:
        print(
            "No se ha modificado el TaTeTi. Causa: un dato fue ingresado de forma incorrecta."
        )
    for i in range(0, len(matriz_tateti)):
        print(matriz_tateti[i])
    seguirJugando = input("Desea seguir jugando? (ingrese 's' para continuar): ")


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.
matriz_de_ventas = [
    [12, 21, 32, 23, 45, 54, 10],
    [54, 45, 67, 76, 78, 87, 12],
    [90, 98, 56, 54, 43, 23, 13],
    [12, 32, 42, 20, 54, 65, 67],
]
total_producto = 0
dia_mayores_ventas_totales = -1
producto_mas_vendido = -1
variable_auxilar = 0
variable_auxilar2 = 0
total_dia = 0

for i in range(0, len(matriz_de_ventas)):
    for j in range(0, len(matriz_de_ventas[0])):
        total_producto += matriz_de_ventas[i][j]
    print(f"El total de ventas del producto {i+1} es: {total_producto}")
    if total_producto > variable_auxilar:
        variable_auxilar = total_producto
        producto_mas_vendido = i
    total_producto = 0
print(
    f"El producto mas vendido de la semana fue el numero: {producto_mas_vendido+1}, con un total de {variable_auxilar}"
)

for i in range(0, len(matriz_de_ventas[0])):
    for j in range(0, len(matriz_de_ventas)):
        total_dia += matriz_de_ventas[j][i]
    if total_dia > variable_auxilar2:
        variable_auxilar2 = total_dia
        dia_mayores_ventas_totales = i
    total_dia = 0
print(
    f"El dia con mayores ventas totales es el numero: {dia_mayores_ventas_totales+1}, con un total de {variable_auxilar2} ventas"
)
