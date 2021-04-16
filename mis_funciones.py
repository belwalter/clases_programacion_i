

def listado(conjunto_datos):
    for persona in conjunto_datos:
        print(persona)


#! variables primitivas inmutables numericas, string, boolean
def suma(num1, num2, total):
    "suma los dos numeros"
    total = num1 + num2


#! cualquiera que no sea primitiva mutables
def agregar(lista, valor):
    """ modifica el valor de la posicion por el valor 0 ingresado"""
    lista[0] = valor

    