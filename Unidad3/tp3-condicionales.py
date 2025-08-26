import random
from statistics import mode, median, mean

# 1)
edad_ingresada = int(input("Ingrese su edad:"))
if edad_ingresada >= 18:
    print("Es Mayor de edad")

# 2)
nota_ingresada = int(input("Ingrese su nota: "))
if nota_ingresada >= 6:
    print("Aprobado")
else:
    "Desaprobado"

# 3)
numero_ingresado = int(input("ingrese un numero par: "))
if numero_ingresado % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

# 4)
edad_ingresada2 = int(input("ingrese su edad: "))
if edad_ingresada2 < 12:
    print("Niño")
elif edad_ingresada2 >= 12 and edad_ingresada2 < 18:
    print("Adolescente")
elif edad_ingresada2 >= 18 and edad_ingresada2 < 30:
    print("Adulto joven")
elif edad_ingresada2 >= 30:
    print("Adulto")

# 5)
password_ingresado = input("ingrese su password de entre 8 y 14 caracteres")
if len(password_ingresado) >= 8 and len(password_ingresado) <= 14:
    print("Ha ingresado un password correcto")
else:
    print("Por favor ingrese un password de entre 8 y 14 caracteres.")

# 6)
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
if mode(numeros_aleatorios) < median(numeros_aleatorios) < mean(numeros_aleatorios):
    print("Sesgo Positivo o a la derecha")
elif mode(numeros_aleatorios) > median(numeros_aleatorios) > mean(numeros_aleatorios):
    print("Sesgo negativo o a la izquierda")
else:
    print("No hay sesgo")

# 7)
string_ingresada = input("ingrese una palabra o frase: ").strip()
ultimo_caracter = string_ingresada[len(string_ingresada) - 1]
if (
    ultimo_caracter.lower() == "a"
    or ultimo_caracter.lower() == "e"
    or ultimo_caracter.lower() == "i"
    or ultimo_caracter.lower() == "o"
    or ultimo_caracter.lower() == "u"
):
    string_ingresada += "!"
print(string_ingresada)

# 8)
nombre_ingresado = input("Ingrese un nombre: ")
print(
    """
1.  Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2.  Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3.  Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
"""
)
numero_ingresado = int(input("Ingrese un numero segun la opcion que quiera:"))
if numero_ingresado == 1:
    nombre_ingresado = nombre_ingresado.upper()
elif numero_ingresado == 2:
    nombre_ingresado = nombre_ingresado.lower()
elif numero_ingresado == 3:
    nombre_ingresado = nombre_ingresado.title()
else:
    nombre_ingresado = "Por favor, ingrese un numero del 1 al 3"
print(f"Respuesta de la App: {nombre_ingresado}")

# 9)
magnitud_ingresada = int(input("ingrese la magnitud del terremoto:"))
if magnitud_ingresada < 3:
    print("Muy leve")
elif magnitud_ingresada >= 3 and magnitud_ingresada < 4:
    print("Leve")
elif magnitud_ingresada >= 4 and magnitud_ingresada < 5:
    print("Moderado")
elif magnitud_ingresada >= 5 and magnitud_ingresada < 6:
    print("Fuerte")
elif magnitud_ingresada >= 6 and magnitud_ingresada < 7:
    print("Muy fuerte")
elif magnitud_ingresada >= 7:
    print("Extremo")

# 10)
hemisferio_ingresado = input("Ingrese su hemisferio(N o S)").upper()
mes_ingresado = int(input("ingrese mes del año"))
dia_ingresado = int(input("Ingrese dia del mes"))
estacion = ""
if hemisferio_ingresado == "N":
    if (mes_ingresado == 12 and dia_ingresado >= 21) or (mes_ingresado in [1, 2]) or (mes_ingresado == 3 and dia_ingresado <= 20):
        estacion = "Invierno"
    elif (mes_ingresado == 3 and dia_ingresado >= 21) or (mes_ingresado in [4, 5]) or (mes_ingresado == 6 and dia_ingresado <= 20):
        estacion = "Primavera"
    elif (mes_ingresado == 6 and dia_ingresado >= 21) or (mes_ingresado in [7, 8]) or (mes_ingresado == 9 and dia_ingresado <= 20):
        estacion = "Verano"
    elif (mes_ingresado == 9 and dia_ingresado >= 21) or (mes_ingresado in [10, 11]) or (mes_ingresado == 12 and dia_ingresado <= 20):
        estacion = "Otoño"
elif hemisferio_ingresado == "S":
    if (mes_ingresado == 12 and dia_ingresado >= 21) or (mes_ingresado in [1, 2]) or (mes_ingresado == 3 and dia_ingresado <= 20):
        estacion = "Verano"
    elif (mes_ingresado == 3 and dia_ingresado >= 21) or (mes_ingresado in [4, 5]) or (mes_ingresado == 6 and dia_ingresado <= 20):
        estacion = "Otoño"
    elif (mes_ingresado == 6 and dia_ingresado >= 21) or (mes_ingresado in [7, 8]) or (mes_ingresado == 9 and dia_ingresado <= 20):
        estacion = "Invierno"
    elif (mes_ingresado == 9 and dia_ingresado >= 21) or (mes_ingresado in [10, 11]) or (mes_ingresado == 12 and dia_ingresado <= 20):
        estacion = "Primavera"
else:
    estacion = "Seleccione N o S para indicar los hemisferios"

print(f"La estacion es: {estacion}")
