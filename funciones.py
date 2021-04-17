


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

def sumatoria(numero):
    suma = 0
    for i in range(1, numero+1):
        suma += 1/i
    return suma