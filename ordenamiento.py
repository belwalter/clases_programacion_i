

def burbuja(lista):
    """Método de ordenamiento burbuja."""
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-i-1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]



datos = [[2, 4, 3], [6, 1, 'abd'], [0, 9]]

# from random import randint

# for i in range(0, 10):
#     datos.append(randint(0, 20))
# print(datos)

# print(4 in datos)



a = ['a', 'b', 'c', 'd']

for index, letra in enumerate(a):
    if(letra == 'b'):
        print(index, letra)

for i in range(len(a)):
    if(a[i]=='b'):
        print(i, a[i])

# print(a[1])