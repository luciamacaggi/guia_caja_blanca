import math

def suma2(x: int, y: int) -> int:
  res: int = x + y
  return print(res)
 
suma2(3,4)

def raizDeDos():
  res = round(math.sqrt(2), 4)
  return print(res)

raizDeDos()

def imprimir_hola():
  return print("Hola")

imprimir_hola()

def imprimir_un_verso():
  print("Mañana es mejor")
  print("A las tres de la mañana")

imprimir_un_verso()

def factorial_de_dos():
  res: int = 1*2
  print(res)

factorial_de_dos()

def imprimir_saludo():
  nombre = input("Diga su nombre: ")
  print("Hola " + nombre)

imprimir_saludo()

def raiz_cuadrada_de():
  x = int(input("Indique el número cuya raiz desea: "))
  res = math.sqrt(x)
  print("El resultado es " + str(res))

raiz_cuadrada_de()

def imprimir_dos_veces():
    estribillo = input("Escribir un estribillo: ")
    print(estribillo)
    print(estribillo)

imprimir_dos_veces()

def es_multiplo_de(x: int, y: int):
    if(int(x) % int(y) == 0):
       res = True
    else:
       res = False
    return res

def es_par():
    numero = input("Quiero saber si es par... ")
    if(es_multiplo_de(numero, 2) == True):
        res = True
    else:
        res = False
    print(res)

es_par()

def cantidad_de_pizzas():
    comensales = input("Indique cantidad de comensales: ")
    porciones = input("Indique cantidad mínima de porciones que cada cual come: ")
    x = int(comensales) * int(porciones)
    if(es_multiplo_de(x, 8) == True):
        res = x / 8 
    else:
        res = math.ceil(x / 8)
    print(str(res))

cantidad_de_pizzas()

def alguno_es_0(numero1: int, numero2: int) -> bool:
    return bool(numero1 == 0 or numero2 == 0) 


def ambos_son_0(numero1: int, numero2: int) -> bool:
    return bool(numero1 == 0 and numero2 == 0)

def es_nombre_largo(nombre: str) -> bool:
    return bool(3 <= len(nombre) <= 8)

def es_bisiesto(año: int) -> bool:
    return bool(es_multiplo_de(año, 400) or (es_multiplo_de(año, 4) and not es_multiplo_de(año, 100)))

def peso_pino(altura_pino: int) -> bool:
    if altura_pino <= 3:
        peso = altura_pino * 100 * 3
    elif altura_pino > 3:
        peso = 900 + ((altura_pino - 3) * 100 * 2)
    return peso

def es_peso_util(peso: int) -> bool:
    return bool(400 <= peso <= 1000)

def sirve_pino(altura_pino: int) -> bool:
    return bool(400 <= peso_pino(altura_pino) <= 1000)

def devolver_el_doble_si_es_par(un_numero: int) -> int:
    if es_multiplo_de(un_numero, 2):
        return un_numero * 2
    else:
        return un_numero
    
def devolver_valor_si_es_par_si_no_el_que_sigue(un_numero: int) -> int:
    return un_numero if es_multiplo_de(un_numero, 2) else un_numero + 1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(un_numero: int) -> int:
    if es_multiplo_de(un_numero, 3):
        return un_numero * 2 
    elif es_multiplo_de(un_numero, 9): # esta condicion nunca va a ser ejecutada pues todo multiplo de 9 es de 3
        return un_numero * 3
    else:
        return un_numero
    
def tu_nombre(nombre: str) -> str:
    nombre: str = input("¿Cómo te llamas? ")
    print("Tu nombre tiene muchas letras!") if len(nombre) >= 5 else print("Tu nombre es cortito")

def tu_vida(sexo: str, edad: int) -> str:
    sexo: str = input("Define tu sexo F o M:")
    edad: int = input("¿Cuántos años tienes? ")
    if int(edad) < 18 or (sexo == "F" and int(edad) >= 60) or (sexo == "M" and int(edad) >= 65):
        print("Ve de vacaciones a divertirte")
    else:
        print("Te toca trabajar cuánto lo siento")

def imprimir_uno_al_diez():
    i = 1
    while i <= 10:
        print(i)
        i += 1

def imprimir_pares_diez_a_cuarenta():
    i = 10
    while i <= 40:
        print(i)
        i +=2

def ecos():
    i = 1
    while i <= 10:
        print("eco")
        i += 1

def cuenta_regresiva():
    i = int(input("Inicie cuenta en: "))
    while i >= 0:
        print(i)
        i -= 1

    print("Despegue")

def viaje_en_el_tiempo(año_partida: int, año_llegada: int) -> str:
    año_partida = int(input("Bienvenido! Indique año de partida que desee: "))
    año_llegada = int(input("A cuándo quiere viajar? "))
    if año_llegada > año_partida:
        print("Disculpe las molestias, por ahora no podemos viajar al futuro")
    else:
        while año_partida >= año_llegada:
            año_presente = año_partida
            print("Viajó un año al pasado, estamos en el año ", str(año_presente))
            año_partida -= 1

def nuevo_viaje_aristotelico(año_partida: int) -> str:
    año_partida: int(input("Abrochen sus cinturones! Desde qué año partimos? "))
    for año_partida in range(año_partida, -385, -20):
        print("Estamos en la estación:", str(año_partida))
    print("¡Enhorabuena, tiempo de conocerlo al maestro Aristóteles!")

def rt(x: int, g: int) -> int: # asegura = (p/t x, g en Z){res = x + g + 1}
    g = g + 1
    return x + g
g: int = 0
def ro(x: int) -> int: # asegura = (p/t x en Z){res = x + 1}
    global g
    g = g + 1
    return x + g