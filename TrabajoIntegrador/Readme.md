# Trabajo Integrador - Programación 1

## Gestión de Países (Python CLI)

## Link del video de presentación:

https://youtu.be/4E3tDD3Qo-s

## Diagrama de flujo del codigo:

https://miro.com/app/board/uXjVJtx2UG0=/

### Descripción del programa

Este proyecto consiste en el desarrollo de un sistema de gestión de información sobre países, programado en Python 3. Permite leer, almacenar, filtrar, ordenar y analizar datos a partir de un archivo CSV.
El objetivo principal es aplicar los conceptos fundamentales de la programación estructurada, como:

- Listas y diccionarios
- Funciones y modularización
- Estructuras condicionales y repetitivas
- Ordenamientos simples y manejo de datos
- Cálculo de estadísticas básicas
- Persistencia de datos mediante archivos CSV

El programa ofrece un menú interactivo por consola, desde el cual el usuario puede:

- Agregar un país con sus datos
- Actualizar población y superficie
- Buscar países por nombre
- Filtrar por continente, rango de población o superficie
- Ordenar los resultados por nombre, población o superficie
- Consultar estadísticas (promedios, mínimos y máximos, conteo por continente)

El dataset se guarda en el archivo dataset_paises.csv, garantizando la persistencia entre ejecuciones.

- El programa guarda automáticamente los cambios al agregar o actualizar un país.
- Si el archivo CSV no existe, se crea con datos iniciales.

### Instrucciones de uso

Requisitos previos:
Tener instalado Python 3.x o superior
Contar con el archivo base dataset_paises.csv (se crea automáticamente la primera vez)

Ejecución:

- Clonar o descargar el repositorio
- Ejecutar el programa

- Seguir las opciones del menú en consola:

1. Mostrar datos
2. Agregar país
3. Actualizar población y superficie
4. Buscar país
5. Filtrar países
6. Ordenar países
7. Mostrar estadísticas
8. Salir

### Ejemplos de entradas y salidas

Ejemplo 1: Agregar país

- Entrada: 2
  Ingrese el nombre del país: Chile
  Ingrese la población del país: 19458310
  Ingrese la superficie del país en km²: 756096
  Ingrese el continente del país: América
- Salida:
  Datos guardados correctamente en el archivo CSV.

Ejemplo 2: Buscar país

- Entrada: 4
  Ingrese el nombre del país que quiere buscar: arg
- Salida:
  País: Argentina - Población: 45376763 - Superficie: 2780400 km² - Continente: América

Ejemplo 3: Mostrar estadísticas

- Entrada: 7

1. País con mayor y menor población
2. Promedio de población
3. Promedio de superficie
4. Cantidad de países por continente
   Ingrese el tipo de estadística que quiere: 2

- Salida:
  El promedio de la población entre los países registrados es de 324.345.891 habitantes

### Participación de los integrantes

Simón Blas – Comisión 2 – Desarrollo del código principal, manejo del archivo CSV, diagramas, pruebas del sistema, redacción de conclusiones, grabación de video, documentación teórica y presentación del informe – simoblas08@gmail.com

Joel Vitrano – Comisión 12 – No realizo aportes

Debido a la falta de respuesta del compañero asignado, el trabajo fue desarrollado y presentado de manera individual por el alumno Simón Blas.