# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.


num_entero = int(input("ingrese un numero entero: "))
cant_dig = 0
num_entero = abs(num_entero)
if num_entero == 0:
    cant_dig = 1
else:
    while num_entero > 0:
        cant_dig = cant_dig + 1
        num_entero = num_entero // 10
print(cant_dig)


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.


num_inicial = int(input("Ingrese el valor inicial de la sumatoria: "))
num_final = int(input("Ingrese el valor final de la sumatoria: "))
num_inicial += 1
valor_sumatoria = 0
for i in range(num_inicial, num_final):
    valor_sumatoria += i
print(valor_sumatoria)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.


total_sumatoria = 0
num_ingresado = None
while num_ingresado != 0:
    num_ingresado = int(input("Ingrese un numero entero: "))
    total_sumatoria += num_ingresado
print(f"el total de la sumatoria es: {total_sumatoria}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random

num_aleatorio = random.randint(0, 9)
num_ingresado = int(input("Ingrese un numero entero entre 0 y 9 (incluidos): "))
cant_intentos = 1
while num_aleatorio != num_ingresado:
    num_ingresado = int(input("Ingrese un nuevo valor entre 0 y 9: "))
    cant_intentos += 1
print(f"La cantidad de intentos fueron: {cant_intentos}")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.


for i in range(100, -1, -2):
    print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.


num_usuario = abs(
    int(input("Ingrese un numero entero positivo para el final de la sumatoria: "))
)
total_sum = 0
for i in range(1, num_usuario + 1):
    total_sum += i
print(f"El total de la sumatoria es: {total_sum}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).


numero_ingresado = None
cont_pares = 0
cont_impares = 0
cont_negativos = 0
cont_positivos = 0
for i in range(100):
    numero_ingresado = int(input("Ingrese un numero entero: "))
    if numero_ingresado % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1
    if numero_ingresado > 0:
        cont_positivos += 1
    elif numero_ingresado < 0:
        cont_negativos += 1
print(
    f"Los numeros registrados son:\n Pares: {cont_pares} \n Impares: {cont_impares} \n Negativos: {cont_negativos} \n Positivos: {cont_positivos}"
)


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).


user_input = 0
media = 0
input_count = 100
for i in range(input_count):
    user_input = int(input("Ingrese un numero entero: "))
    media += user_input
media = media / input_count
print(f"La media de los numeros ingresados es: {media}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
input_number = int(input("Ingrese un numero: "))
auxiliar = 0
numero_invertido = 0
digitos_totales = 0
contenedor_numero_ingresado = input_number

if input_number == 0:
    digitos_totales = 1
else:
    while abs(input_number) > 0:
        digitos_totales += 1
        input_number = input_number // 10

if digitos_totales == 1:
    print(
        f"El numero ingresado solo tiene 1 digito, por lo tanto sigue siendo el mismo: {contenedor_numero_ingresado}"
    )
else:
    for i in range(0, digitos_totales):
        auxiliar = contenedor_numero_ingresado % 10
        contenedor_numero_ingresado = contenedor_numero_ingresado // 10
        numero_invertido = numero_invertido * 10 + auxiliar
    print(f"El numero invertido es: {numero_invertido}")
