


def positivo_negativo(numero):
    """determinar si el numero es positivo(devuelve true) o negativo( devuelve falso)"""
    if(numero>=0):
        return True
    else:
        return False



def contar_caracter(cadena, caracter):
    """contar cuantas veces aparece el caracter en la cadena"""
    cantidad = 0
    for letra in cadena:
        if(letra == caracter):
            cantidad += 1
    return cantidad
    
def es_palindromo(cadena):
    """determina si una cadena es palindromo"""
    cadena_aux = list(cadena)
    cadena_aux.reverse()
    cadena_invertida = ''
    cadena_invertida = cadena_invertida.join(cadena_aux)

    return cadena_invertida == cadena

# def sumatoria(numero):
#     suma = 0
#     for i in range(1, numero+1):
#         suma += 1/i
#     return suma


def cargar_datos():
    """doctring de la funcion"""
    nombre = input('ingrese su nombre ')
    return nombre


def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def producto(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    return numero1 / numero2


def potencia(base, exponente):
    return base ** exponente

operaciones = {'+' : suma, '-': resta, '*' : producto, '/': division, '^':potencia}



def calculadora(numero1, operador, numero2):
    if(operador in operaciones):
        return operaciones[operador](numero1, numero2)
    else:
        return None


def es_vocal(caracter):
    vocales = ['a', 'e', 'i', 'o', 'u']
    return caracter.lower() in vocales


def sumatoria(numero):
    total = 0
    for i in range(1, numero+1):
        total += 1/i

    return total

# print(sumatoria(100))

# for i in range(1,10+1):
#     print(i)

# num1 = int(input('ingrese un valor '))
# operador = input('ingrese un operador ')
# num2 = int(input('ingrese un valor '))

# control = True

# while(control):
#     num1 = calculadora(num1, operador, num2)
#     print(num1)
#     operador = input('ingrese un operador ')
#     if(operador == '?'):
#         control = False
#     num2 = int(input('ingrese un valor '))
