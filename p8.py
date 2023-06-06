def pertenece(s: list, e: int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    else:
        return False
    
###

def divide_a_todos(s: list, e: int) -> bool:
    for i in range(len(s)):
        if s[i] % e == 0:
            res = True
        else:
            res = False
            return res
    return res

###        

def suma_total(s: list) -> int:
    suma = 0
    for i in range(len(s)):
        x = s[i] + suma
        suma = x
    return suma

###

def ordenados(s: list) -> bool:
    if len(s) <= 1:
        res = "Tu lista es muy pequeña o inexistente"
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            res = True
        else:
            res = False
            return res
    return res

###

def muchas_palabras(l: list) -> bool:
    check = []
    for i in range(len(l)):
        if len(l[i]) > 7:
            check.append(True)
        else:
            check.append(False)
    return any(check)

###

def palindroma(p: str) -> bool:
    j = int(len(p) - 1)
    for i in range(len(p)):
        if p[i] == p[j] and i < j:
            i += 1
            j -= 1
        elif i >= j:
            res = True
            return res
        else:
            res = False
            return res
        
###

def contra_fuerte(c: str) -> str:
    if len(c) > 5:
        mayus = []
        minus = []
        numero = []
        for i in range(len(c)):
            mayus.append(c[i].isupper())
            minus.append(c[i].islower())
            numero.append(es_numero(c[i]))
        res = bool(any(mayus) and any(minus) and any(numero))
        if res == True:
            return "Verde" if len(c) > 8 else "Roja"
        else:
            return "Amarilla"
    else:
        return "Amarilla"

def es_numero(n: int) -> bool:
    return True if n in ["0","1","2","3","4","5","6","7","8","9"] else False

###

def ver_saldo(l: list) -> int:
    sumar = []
    restar = []
    for i in range(len(l)):
        if str(l[i][0]) == str("R"):
            restar.append(l[i][1])
        else:
            sumar.append(l[i][1])
    return suma_total(sumar) - suma_total(restar)

###

# Funciones auxiliares
def es_vocal(l: str) -> bool:
    return True if l in ["a","e","i","o","u"] else False

def eliminar_reps(a: list) -> list:
    sin_reps = [a[0]]
    for k in range(len(a)):
        esta_o_no = []
        for l in range(len(sin_reps)):
            if a[k] != sin_reps[l]:
                esta_o_no.append(True)
            else:
                esta_o_no.append(False)
        if all(esta_o_no):
            sin_reps.append(a[k])
        else:
            continue
    return sin_reps
# Funcion del ejercicio
def tiene_tres_vocales(p: str) -> bool:
    vocales = []
    vocales_sin_reps = []
    for i in range(len(p)):
        if es_vocal(p[i]) or es_vocal((p[i]).lower()) == True:
            vocales.append(p[i])
    vocales_sin_reps = eliminar_reps(vocales)
    if len(vocales_sin_reps) >= 3:
        return True
    else:
        return False

###

# Funciones auxiliares
def es_multiplo_de(x: int, y: int) -> bool:
    if int(x) % int(y) == 0:
       res = True
    else:
       res = False
    return res

def es_par(numero: int) -> bool:
    if es_multiplo_de(numero, 2) == True:
        res = True
    else:
        res = False
    return res
# Funcion del ejercicio
def pares_por_ceros(l: list) -> list: # Qué significa que la lista sea un tipo inout?
    nueva_lista = []
    for i in range(len(l)):
        if es_par(int(l[i])) == True:
            nueva_lista.append(0)
        else:
            nueva_lista.append(l[i])
    return nueva_lista

###

# Funcion auxiliar
def es_vocal(l: str) -> bool:
    return True if l in ["a","e","i","o","u"] else False
# Funcion del ejercicio (segunda parte 2: 3.)
def texto_sin_vocales(p: str) -> str:
    a = ""
    for i in range(len(p)):
        if es_vocal(p[i]) or es_vocal((p[i]).lower()) == True:
            continue
        else:
            a = a + p[i]
            b = a       
    return b
# Funcion del ejercicio (segunda parte 2: 4.)
def reemplaza_vocales(p: str) -> str:
    a = ""
    for i in range(len(p)):
        if es_vocal(p[i]) or es_vocal((p[i]).lower()) == True:
            a = a + "_"
            b = a
        else:
            a = a + p[i]
            b = a
    return b

###

def dar_vuelta(p: str) -> str:
    a = p[(len(p)-1)]
    for i in range(len(p) - 2, -1, -1):
        a = a + p[i]
        b = a
    return b

###

# Falta hacer segunda parte 3 y 4