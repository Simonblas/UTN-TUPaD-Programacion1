# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario


def factorial_recur(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recur(num - 1)


def ej1():
    num_ingresado = int(
        input("Indique hasta que numero calcular los factoriales: ").strip()
    )
    if num_ingresado < 0:
        print("Ingrese un numero entero positivo (puede ser 0).")
    else:
        for i in range(0, num_ingresado + 1):
            print(f"Numero: {i}, factorial: {factorial_recur(i)}")
    return


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.
def fibonacci_recursiva(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursiva(num - 1) + fibonacci_recursiva(num - 2)


def ej2():
    num_ingresado = int(
        input(
            "Ingrese el numero de la posicion final de fibonacci a calcular: "
        ).strip()
    )
    for i in range(0, num_ingresado + 1):
        print(f"Posicion {i}, valor fibonacci: {fibonacci_recursiva(i)}")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛∗𝑛^(𝑚−1). Prueba esta función en un
# algoritmo general.
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)


def ej3():
    base = int(input("Ingrese el numero de la base: ").strip())
    exponente = int(input("Ingrese el numero del exponente: ").strip())
    print(potencia_recursiva(base, exponente))


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
def decimal_a_binario_recursiva(num_decimal, numero_binario):
    if num_decimal == 1:
        numero_binario = "1" + numero_binario
        return numero_binario
    elif num_decimal == 0:
        if numero_binario == "":
            return "0"
        else:
            return numero_binario
    else:
        numero_binario = f"{num_decimal % 2}" + numero_binario
        return decimal_a_binario_recursiva(num_decimal // 2, numero_binario)


def ej4():
    num_ingresado = int(
        input("Ingrese un numero decimal para pasarlo a binario: ").strip()
    )
    numero_binario = ""
    print(decimal_a_binario_recursiva(num_ingresado, numero_binario))


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#      Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().


def es_palindromo_recursiva(palabra):
    es_palindromo = False
    if len(palabra) <= 1:
        es_palindromo = True
        return es_palindromo
    elif palabra[0] != palabra[len(palabra) - 1]:
        es_palindromo = False
        return es_palindromo
    else:
        palabra2 = palabra[1:-1]
        es_palindromo = True
        return es_palindromo_recursiva(palabra2)


def ej5():
    palabra_ingresada = input(
        "Ingrese una palabra para verificar si es palindromo: "
    ).strip()
    if palabra_ingresada == "":
        print("el campo no puede estar vacio.")
    else:
        if es_palindromo_recursiva(palabra_ingresada):
            print("La palabra ingresada es Palindromo.")
        else:
            print("La palabra ingresada NO es palindromo")


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
def suma_digitos_recursiva(num):
    if num // 10 == 0:
        return num
    else:
        return (num % 10) + int(suma_digitos_recursiva(num // 10))


def ej6():
    num_ingresado = int(
        input("Ingrese un numero para calcular la suma de sus digitos: ").strip()
    )
    print(f"La suma es: {suma_digitos_recursiva(num_ingresado)}")


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.


# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
def contar_bloques_recursiva(base_piramide, total_acumulado):
    if base_piramide == 1:
        total_acumulado += base_piramide
        return total_acumulado
    else:
        total_acumulado += base_piramide
        base_piramide -= 1
        return contar_bloques_recursiva(base_piramide, total_acumulado)


def ej7():
    base_piramide = int(input("Ingrese la base de la piramide: ").strip())
    total_acumulado = 0
    print(
        f"El total de bloques para construir la piramide es: {contar_bloques_recursiva(base_piramide, total_acumulado)}"
    )


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
def contar_digito_recursiva(num, digito, cantidad_rep):
    if num // 10 == 0:
        if num == digito:
            cantidad_rep += 1
        return cantidad_rep
    else:
        if num % 10 == digito:
            cantidad_rep += 1
        num = num // 10
        return contar_digito_recursiva(num, digito, cantidad_rep)


def ej8():
    num_ingresado = int(input("Ingrese un numero entero: ").strip())
    digito_ingresado = int(input("Ingrese un digito: ").strip())
    print(
        f"La cantidad de digitos en el numero ingresado es: {contar_digito_recursiva(num_ingresado, digito_ingresado, cantidad_rep=0)}"
    )
