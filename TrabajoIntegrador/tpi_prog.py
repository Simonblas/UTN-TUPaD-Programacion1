# TRABAJO PRACTICO INTEGRADOR DE PROGRAMACION 1
# DIAGRAMA DE FLUJO DEL CODIGO:
# https://miro.com/app/board/uXjVJtx2UG0=/
import csv
import os


# funcion que usaremos para traer el dataset que tenemos en el archivo CSV
def obtener_dataset():
    dataset = []
    # si no existe el csv del dataset, lo creamos con los datos bases.
    if not os.path.exists("dataset_paises.csv"):
        # usamos una matriz para indicar los datos y encabezado que escribira nuestro escritor csv
        datos = [
            ["nombre", "poblacion", "superficie", "continente"],
            ["Argentina", 45376763, 2780400, "América"],
            ["Japón", 125800000, 377975, "Asia"],
            ["Brasil", 213993437, 8515767, "América"],
            ["Alemania", 83149300, 357022, "Europa"],
        ]
        # newline y encoding nos sirven para evitar errores de formatos con windows
        with open("dataset_paises.csv", "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(datos)
        print(
            "El catalogo no existia, por lo que ha sido creado con los datos iniciales correspondientes."
        )
    # si el archivo ya existia, leemos los datos que guarda
    else:
        # DictReader nos lee cada fila como un diccionario, usando el encabezado como claves
        # lo que permite ahorrarnos pasos de iteracion para el guardado de los datos.
        with open("dataset_paises.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # casteamos los valores de poblacion y superficie a enteros
                fila["poblacion"] = int(fila["poblacion"])
                fila["superficie"] = int(fila["superficie"])
                dataset.append(fila)
    return dataset


# funcion que usaremos para ir guardando el dataset en el archivo.csv cuando sea necesario
def guardar_dataset(dataset):
    if not dataset:
        print("No hay datos para guardar en el archivo CSV.")
        return
    # le indicamos que columnas debe escribir nuestro DictWriter
    # usara el encabezado como claves para ir escribiendo las columnas de forma ordenada
    campos = dataset[0].keys()
    with open("dataset_paises.csv", "w", encoding="utf-8", newline="") as archivo:
        # con fieldnames indicamos el nombre de cada campo (columna) para que mantenga consistencia
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()  # escribe el encabezado
        escritor.writerows(
            dataset
        )  # ignora el encabezado y escribe los datos del dataset
    print("Datos guardados correctamente en el archivo CSV.")
    return


# permite mostrar todos los paises junto a sus datos
def mostrar_dataset():
    dataset = obtener_dataset()
    if len(dataset) == 0:
        print("El archivo de datos esta vacio.")
    else:
        print("\n Datos que guardaba el archivo CSV: \n")
        for fila in dataset:
            print(
                f'pais: {fila["nombre"]}  -  poblacion: {fila["poblacion"]}  -  superficie: {fila["superficie"]} km²  -  continente: {fila["continente"]}\n'
            )
    return


# permite agregar un pais con los datos necesarios para almacenarse (nombre, poblacion, superficie, continente) NO se permiten campos vacios
def agregar_pais(nombre, poblacion, superficie, continente):
    dataset = obtener_dataset()
    # verificamos que no haya duplicados.
    for pais in dataset:
        if pais["nombre"].lower() == nombre.lower():
            print("El pais ya existe en el dataset")
            return
    # si no hay duplicados, lo agrega correctamente.
    dataset.append(
        {
            "nombre": nombre,
            "poblacion": int(poblacion),
            "superficie": int(superficie),
            "continente": continente,
        }
    )
    guardar_dataset(dataset)


# permite buscar un pais por su nombre y actualizar su poblacion y superficie
def actualizar_datos(nombre_pais, poblacion, superficie):
    # recibe nombre como string, poblacion como Int y superficie como Int
    dataset = obtener_dataset()
    coincidencia = False
    # verificamos que coincida con un pais guardado
    for pais in dataset:
        if pais["nombre"].lower() == nombre_pais.lower():
            pais["poblacion"] = poblacion
            pais["superficie"] = superficie
            coincidencia = True
    if coincidencia:
        print("Actualizamos los datos correctamente")
        guardar_dataset(dataset)
    else:
        print(
            "No hemos encontrado un pais que coincida con el nombre ingresado. Intentelo nuevamente."
        )


# permite buscar un pais por nombre (coincidencia parcial o exacta)
def buscar_pais(nombre):
    # recibe el nombre del pais como string
    dataset = obtener_dataset()
    coincidencias = []
    # confirmamos que el nombre ingresado quepa en el nombre de algun pais
    for pais in dataset:
        if nombre.lower() in pais["nombre"].lower():
            coincidencias.append(pais)
    if len(coincidencias) > 0:
        for pais in coincidencias:
            print(
                f'\npais: {pais["nombre"]}  -  poblacion: {pais["poblacion"]}  -  superficie: {pais["superficie"]} km²  -  continente: {pais["continente"]}\n'
            )
    else:
        print("No hemos encontrado coincidencias con el nombre ingresado.")


# permite filtrar paises por continente//rango de poblacion//rango de superficie.
def filtrar_paises(tipo_filtro):
    # tipo_filtro recibira un string "continente"//"poblacion"//"superficie"
    dataset = obtener_dataset()
    filtro = []
    match tipo_filtro:
        # dependiendo el caso a filtrar, procedemos de distintas formas
        case "continente":
            continente = input(
                "Ingrese el continente a filtrar (Permitimos busqueda parcial para evitar errores de tildes): "
            ).strip()
            if continente:
                for pais in dataset:  # agregamos al filtro los valores validos.
                    # en este caso tambien lo haremos de forma parcial, para poder filtrar de forma mas eficiente por ejemplo:
                    # am para america y que se filtren los paises que tengan América y America como continente.
                    if continente.lower() in pais["continente"].lower():
                        filtro.append(pais)
            else:
                print("El campo del continente no puede estar vacio.")

        case "poblacion":
            min_poblacion = input("Ingrese el minimo de poblacion: ").strip()
            max_poblacion = input("Ingrese el maximo de poblacion: ").strip()
            # casteamos el tipo de dato a entero para continuar correctamente.
            if min_poblacion.isdigit() and max_poblacion.isdigit():
                min_poblacion = int(min_poblacion)
                max_poblacion = int(max_poblacion)
                if min_poblacion < max_poblacion:
                    for pais in dataset:  # agregamos al filtro los valores validos.
                        if min_poblacion < pais["poblacion"] < max_poblacion:
                            filtro.append(pais)
                else:
                    print("El minimo de poblacion no puede superar el maximo.")
            else:
                print(
                    "El minimo y maximo de poblacion deben ser valores numericos enteros."
                )

        case "superficie":
            min_superficie = input("Ingrese el minimo de superficie en km²: ").strip()
            max_superficie = input("Ingrese el maximo de superficie en km²: ").strip()
            # casteamos el tipo de dato a entero para continuar correctamente.
            if min_superficie.isdigit() and max_superficie.isdigit():
                min_superficie = int(min_superficie)
                max_superficie = int(max_superficie)
                if min_superficie < max_superficie:
                    for pais in dataset:  # agregamos al filtro los valores validos.
                        if min_superficie < pais["superficie"] < max_superficie:
                            filtro.append(pais)
                else:
                    print("El minimo de superficie no puede ser mayor que el maximo.")
            else:
                print(
                    "El minimo y maximo de superficie deben ser valores numericos enteros."
                )
    if len(filtro) > 0:
        for pais in filtro:
            print(
                f'\npais: {pais["nombre"]}  -  poblacion: {pais["poblacion"]}  -  superficie: {pais["superficie"]} km²  -  continente: {pais["continente"]}'
            )
    else:
        print("No encontramos paises que coincidan con los datos ingresados.")
    # limpiamos el filtro para poder utilizarlo cuantas veces queramos.
    filtro = []


# permite ordenar paises por nombre//poblacion//superficie (ascendente o descendente)
def ordenar_paises(tipo_orden):
    # Se hara con el ordenamiento burbuja, aunque Python permite utilizar la funcion sorted() para agilizar el trabajo.
    dataset = obtener_dataset()
    # si el tipo de orden es por superficie, debemos pedirle al usuario que indique si debe ordenarse de forma ascendente o descendente
    match tipo_orden:

        case "nombre":
            # asignamos a n la longitud del dataset
            n = len(dataset)
            for i in range(n - 1):  # por cada pais del dataset
                for j in range(0, n - i - 1):  # recorremos los paises restantes
                    if (
                        dataset[j]["nombre"].lower() > dataset[j + 1]["nombre"].lower()
                    ):  # si el pais siguiente es mayor que el actual, los ordenamos.
                        dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
            print("\nPaises ordenados por nombre A-Z:\n")
            for pais in dataset:
                print(
                    f'pais: {pais["nombre"]}  -  poblacion: {pais["poblacion"]}  -  superficie: {pais["superficie"]} km²  -  continente: {pais["continente"]}\n'
                )

        case "poblacion":
            # mismo metodo que con el orden por nombre
            n = len(dataset)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if dataset[j]["poblacion"] > dataset[j + 1]["poblacion"]:
                        dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
            print("\nPaises ordenados por poblacion de menor a mayor:\n")
            for pais in dataset:
                print(
                    f'pais: {pais["nombre"]}  -  poblacion: {pais["poblacion"]}  -  superficie: {pais["superficie"]} km²  -  continente: {pais["continente"]}\n'
                )

        case "superficie":
            forma_orden = input(
                "Indique la forma de ordenamiento Ascendente o Descendente(A/D): "
            ).strip()
            n = len(dataset)
            # dependiendo el tipo de orden elegido por el usuario, ejecutamos un bloque de codigo.
            if forma_orden.upper() == "A":  # si es de forma ascendente
                for i in range(
                    n - 1
                ):  # hacemos nuevamente un ordenamiento burbuja en orden ascendente
                    for j in range(0, n - i - 1):
                        if dataset[j]["superficie"] > dataset[j + 1]["superficie"]:
                            dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
                print("\nPaises ordenados por superficie de forma ascendente:\n")
            elif forma_orden.upper() == "D":  # si es de forma descendente
                for i in range(
                    n - 1
                ):  # hacemos nuevamente un ordenamiento burbuja en orden descendente
                    for j in range(0, n - i - 1):
                        if dataset[j]["superficie"] < dataset[j + 1]["superficie"]:
                            dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
                print("\nPaises ordenados por superficie de forma descendente:\n")
            else:
                print("La opcion ingresada no es valida. Volveremos al menu principal.")
                return

            for pais in dataset:
                print(
                    f'pais: {pais["nombre"]}  -  poblacion: {pais["poblacion"]}  -  superficie: {pais["superficie"]} km²  -  continente: {pais["continente"]}\n'
                )


# permite mostrar las estadisticas de: pais con mayor y menor poblacion//promedio de poblacion//promedio de superficie//cantidad de paises por continente
def mostrar_estadisticas(tipo_estadistica):
    # tipo_estadistica recibira: "mayor_menor_poblacion" // "promedio_poblacion" // "promedio_superficie" // "paises_por_continente"
    dataset = obtener_dataset()
    match tipo_estadistica:

        case "mayor_menor_poblacion":
            if len(dataset) == 0:
                print("Aun no hay datos cargados.")
                return
            mayor = dataset[0]
            menor = dataset[0]
            # recorrer lista para ir comparando poblaciones
            for pais in dataset:
                # aplicamos la misma logica con ambas variables, (vamos ajustando segun los valores correspondientes)
                if pais["poblacion"] > mayor["poblacion"]:
                    mayor = pais
                if pais["poblacion"] < menor["poblacion"]:
                    menor = pais
            print("\nPais con menor poblacion:")
            print(
                f'{menor["nombre"]}  -  poblacion: {menor["poblacion"]}  -  superficie: {menor["superficie"]} km²  -  continente: {menor["continente"]}\n'
            )
            print("Pais con mayor poblacion:")
            print(
                f'{mayor["nombre"]}  -  poblacion: {mayor["poblacion"]}  -  superficie: {mayor["superficie"]} km²  -  continente: {mayor["continente"]}\n'
            )

        case "promedio_poblacion":
            if len(dataset) == 0:
                print("No hay datos cargados.")
                return
            sumatoria = 0
            # realizamos la suma de todos los habitantes y los dividimos por la cantidad de paises.
            for pais in dataset:
                sumatoria += pais["poblacion"]
            promedio = sumatoria / len(dataset)
            # redondeamos ese promedio para que solo tenga 1 decimal.
            print(
                f"\n El promedio de la poblacion entre los paises registrados es de {round(promedio, 1)} habitantes"
            )

        case "promedio_superficie":
            # mismo procedimiento que con el promedio de poblacion
            if len(dataset) == 0:
                print("No hay datos cargados.")
                return
            sumatoria = 0
            for pais in dataset:
                sumatoria += pais["superficie"]
            promedio = sumatoria / len(dataset)
            print(f"\n El promedio de superficie es de {round(promedio, 1)} km².")

        case "paises_por_continente":
            if len(dataset) == 0:
                print("No hay datos cargados.")
                return
            # usaremos un diccionario para acumular los resultados
            cantidad = {}
            for pais in dataset:
                continente = pais[
                    "continente"
                ]  # guardamos el continente del pais recorrido
                if (
                    continente in cantidad
                ):  # si el continente ya existe en nuestro diccionario, le sumamos 1 pais
                    cantidad[continente] += 1
                else:  # si no existe el continente, lo agregamos con valor 1
                    cantidad[continente] = 1
            print("\n La cantidad de paises por continente es: \n")
            # utilizamos continente como clave y total_paises como valor (para mostrarlo luego) ya que cantidad.items nos devuelve elementos pares(clave,valor)
            for continente, total_paises in cantidad.items():
                print(f"El total de paises en {continente} es de {total_paises}.")


def mostrar_menu():
    condicion = 1
    while condicion == 1:
        print("*" * 45)
        print("1. Mostrar datos")
        print("2. Agregar pais")
        print("3. Actualizar poblacion y superficie de un pais")
        print("4. Buscar pais por nombre")
        print("5. Filtrar paises")
        print("6. Ordenar paises")
        print("7. Mostrar estadisticas")
        print("8. Salir de la aplicacion")
        print("*" * 45)
        opcion = input("Ingrese una opcion: ").strip()
        match opcion:

            case "1":
                mostrar_dataset()

            case "2":
                nombre = input("Ingrese el nombre del pais: ").strip()
                poblacion = input("Ingrese la poblacion del pais: ").strip()
                superficie = input("Ingrese la superficie del pais en km²: ").strip()
                continente = input("Ingrese el continente del pais: ").strip()
                while (
                    nombre == ""
                    or continente == ""
                    or superficie == ""
                    or poblacion == ""
                    or not poblacion.isdigit()
                    or not superficie.isdigit()
                ):
                    print(
                        "Ninguno de los campos puede estar vacio. Ademas, la poblacion y superficie deben ser Numeros."
                    )
                    nombre = input("Ingrese el nombre del pais: ").strip()
                    poblacion = input("Ingrese la poblacion del pais: ").strip()
                    superficie = input(
                        "Ingrese la superficie del pais en km²: "
                    ).strip()
                    continente = input("Ingrese el continente del pais: ").strip()
                agregar_pais(nombre, int(poblacion), int(superficie), continente)

            case "3":
                nombre_pais = input(
                    "Ingrese el nombre del pais que quiere actualizar: "
                ).strip()
                poblacion = input("Ingrese la nueva poblacion del pais: ").strip()
                superficie = input(
                    "Ingrese la nueva superficie del pais en km²: "
                ).strip()
                while (
                    nombre_pais == ""
                    or poblacion == ""
                    or superficie == ""
                    or not poblacion.isdigit()
                    or not superficie.isdigit()
                ):
                    print(
                        "Ninguno de los campos puede estar vacio. Ademas, la poblacion y superficie deben ser Numeros."
                    )
                    nombre_pais = input(
                        "Ingrese el nombre del pais que quiere actualizar: "
                    ).strip()
                    poblacion = input("Ingrese la nueva poblacion del pais: ").strip()
                    superficie = input(
                        "Ingrese la nueva superficie del pais en km²: "
                    ).strip()
                actualizar_datos(nombre_pais, int(poblacion), int(superficie))

            case "4":
                nombre = input("Ingrese el nombre del pais que quiere buscar: ").strip()
                while nombre == "":
                    print("El campo no puede estar vacio.")
                    nombre = input(
                        "Ingrese el nombre del pais que quiere buscar: "
                    ).strip()
                else:
                    buscar_pais(nombre)

            case "5":
                print("1. Filtrar por continente")
                print("2. Filtrar por rango de poblacion")
                print("3. Filtrar por rango de superficie")
                tipo_filtro = input("Indique el tipo de filtro: ").strip()
                match tipo_filtro:
                    case "1":
                        tipo_filtro = "continente"
                        filtrar_paises(tipo_filtro)
                    case "2":
                        tipo_filtro = "poblacion"
                        filtrar_paises(tipo_filtro)
                    case "3":
                        tipo_filtro = "superficie"
                        filtrar_paises(tipo_filtro)
                    case _:
                        print(
                            "La opcion ingresada es invalida, vuelva a ingresar para reintentarlo."
                        )

            case "6":
                print("1. Ordenar por nombre")
                print("2. Ordenar por poblacion")
                print("3. Ordenar por superficie")
                tipo_orden = input("Indique el tipo de orden: ").strip()
                while tipo_orden == "" or (
                    tipo_orden != "1" and tipo_orden != "2" and tipo_orden != "3"
                ):
                    print("La opcion ingresada es invalida, vuelva a intentarlo.")
                    tipo_orden = input("Indique el tipo de orden: ").strip()
                else:
                    match tipo_orden:
                        case "1":
                            tipo_orden = "nombre"
                            ordenar_paises(tipo_orden)
                        case "2":
                            tipo_orden = "poblacion"
                            ordenar_paises(tipo_orden)
                        case "3":
                            tipo_orden = "superficie"
                            ordenar_paises(tipo_orden)
            case "7":
                print("1. Pais con mayor y menor poblacion")
                print("2. Promedio de poblacion")
                print("3. Promedio de superficie")
                print("4. Cantidad de paises por continente")
                tipo_estadistica = input(
                    "Ingrese el tipo de estadistica que quiere: "
                ).strip()
                while tipo_estadistica == "" or (
                    tipo_estadistica != "1"
                    and tipo_estadistica != "2"
                    and tipo_estadistica != "3"
                    and tipo_estadistica != "4"
                ):
                    print("La opcion ingresada es invalida, vuelva a intentarlo.")
                    tipo_estadistica = input(
                        "Ingrese el tipo de estadistica que quiere: "
                    ).strip()
                else:
                    match tipo_estadistica:
                        case "1":
                            tipo_estadistica = "mayor_menor_poblacion"
                            mostrar_estadisticas(tipo_estadistica)
                        case "2":
                            tipo_estadistica = "promedio_poblacion"
                            mostrar_estadisticas(tipo_estadistica)
                        case "3":
                            tipo_estadistica = "promedio_superficie"
                            mostrar_estadisticas(tipo_estadistica)
                        case "4":
                            tipo_estadistica = "paises_por_continente"
                            mostrar_estadisticas(tipo_estadistica)
            case "8":
                print("Saliendo de la aplicacion...")
                condicion = 0
                print("Gracias por utilizarla!")

            case _:
                print("La opcion ingresada no es valida, vuelva a intentarlo.")
    return


mostrar_menu()
