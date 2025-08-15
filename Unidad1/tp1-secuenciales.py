import math
# 1)
print("Hola Mundo!")

# 2)
nombre = input("Por favor, ingrese su nombre")
print(f"Hola {nombre}!")

# 3)
nombre = input("ingrese su nombre")
apellido = input("ingrese su apellido")
edad = input("ingrese su edad")
residencia = input("ingrese su residencia")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4)
radio = input("ingrese el radio de un circulo:")
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"el area del circulo es: {area} y el perimetro es: {perimetro}")

# 5)
cantidadSegundos = int(input("ingrese una cantidad de segundos:"))
cantidadMinutos = cantidadSegundos / 60
cantidadHoras = cantidadMinutos / 60
print(f"esos segundos equivalen a {cantidadHoras}")

# 6)
numero = input("ingrese un numero")
for i in range(0, 10):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 7)
num1 = int(input("Ingrese el primer numero distinto de 0:"))
num2 = int(input("Ingrese el segundo numero distinto de 0:"))
if num1 != 0 and num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
    print(f"División: {num1} / {num2} = {division}")
else:
    print("Ambos números deben ser distintos de 0.")

# 8)
altura = int(input("ingrese su altura en metros"))
peso = int(input("ingrese su peso en kg"))
IMC = peso / (altura * altura)
print(f"el imc es: {IMC}")

# 9)
celsius = input("ingrese una temperatura en grados celsius:")
temperaturaFarenheit = (9/5) * celsius + 32
print(temperaturaFarenheit)

# 10)
numero1 = input("ingrese 1er numero")
numero2 = input("ingrese 2do numero")
numero3 = input("ingrese 3er numero")
promedio = (numero1 + numero2 + numero3)/3
print(f"el promedio es: {promedio}")