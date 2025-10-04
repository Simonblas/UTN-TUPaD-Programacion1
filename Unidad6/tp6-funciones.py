import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.


def imprimir_hola_mundo():
    print("Hola Mundo!")


imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.


def saludar_usuario(nombre):
    return f"Hola {nombre}!"


nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
# dir los datos al usuario y llamar a esta función con los valores in-
# gresados.


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
# dio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuel-
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return math.pi * (radio**2)


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


radio = int(input("Ingrese el radio de la circunferencia: "))

print(calcular_area_circulo(radio))

print(calcular_perimetro_circulo(radio))

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función.


def segundos_a_horas(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    return horas


segundos = int(input("Ingrese una cantidad de segundos: "))
print(segundos_a_horas(segundos))


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción.
def tabla_multiplicar(num):
    print(f"La tabla de multiplicar del numero {num} es: ")
    resultado = 0
    for i in range(0, 10):
        resultado = i * num
        print(f"{num} x {i} = {resultado}")
        resultado = 0


num = int(input("Ingrese un numero: "))
tabla_multiplicar(num)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
# sultados de forma clara.


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b
    resultados = (suma, resta, multiplicacion, division)
    return resultados


a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

tuplaResultados = operaciones_basicas(a, b)

print(
    f"Suma: {tuplaResultados[0]} Resta: {tuplaResultados[1]} Multiplicacion: {tuplaResultados[2]} Division: {tuplaResultados[3]}"
)


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso / altura**2
    return round(imc, 2)


peso = float(input("Indique su peso en kg: "))
altura = float(input("Indique su altura en metros: "))
print(f"Su indice de masa corporal es: {calcular_imc(peso, altura)}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.


def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


grados = int(input("Ingrese los grados celsius: "))
print(f"{grados}° celsius en fahrenheit son: {celsius_a_fahrenheit(grados)}")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.


def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
print(f"El promedio es: {calcular_promedio(num1, num2, num3)}")
