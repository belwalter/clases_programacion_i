
#! robias gonzalez presente 

#! CICLOS - FUNCIONES y MODULOS - ESTRUCTURAS DE DATOS - STRING

#! Array o vectores (estatico) --> Listas dinamicas

datos = [2, 3, 4, 7, 0, 1, 56, 6] 

#! Ciclos while (condicionado) for (finito)

# nombre = input('ingrese su nombre ')

# while(nombre != '' and nombre != 'carlos'):
#     print('hola', nombre)
#     nombre = input('ingrese su nombre ')

# for i in range(0, 6):
#     nombre = input('ingrese su nombre ')
#     print(i, nombre)

# if(100 in datos):
#     print('esta en la lista')
# else:
#     print('no esta en la lista')


# for numero in datos:
#     if(numero == 45):
#         print('45 esta en la lista')











# nombre = input('ingrese nombre de persona ').capitalize()

# datos.append(nombre)
# datos.append('Ana')
# datos.append('julieta')
# datos.insert(6, 'Mariano')
# datos.reverse()
# datos.sort()
# datos.remove("carlos")
# print(type(datos), len(datos))
# datos[4] = 100
# print(datos)
# cadena = "   hola MUNDO  desde     python     con vs code"

# print(cadena.capitalize())
# print(cadena.title())
# print(cadena.upper())
# print(cadena.lower())
# print(cadena.replace("o", 'r'))
# print(cadena.split())
# print(cadena.split('o'))
# print(cadena.rstrip())
# print(cadena.find('python2'))
# print(len(cadena))


# if("mundo" == 'Mundo'):
#     print('verdadero')
# else:
#     print('falso')

# nombre = input('ingrese su nombre ').title().split()
# print(nombre) 

# if(nombre == 'Juan'):
#     print('algo')

# cantidad = 18

# for i in range(0, cantidad):

#     numero = int(input('ingrese un numero '))

#     if(numero % 2 == 0 and numero % 3 == 0):
#         print('es multiplo de 2 y de 3')

# datos = []

# for i in range (0, 3):
#     nombre = input("ingrese su nombre ").capitalize()
#     anio_nacimiento = int(input("ingrese año de nacimiento "))

#     edad = 2021 - anio_nacimiento

#     datos.append([nombre, edad])
#     if(edad >= 18):
#         print(nombre,"ES MAYOR DE EDAD")
#     else:
#         print('es menor de edad')

# for persona in datos:
#     print(persona[0], persona[1])

# #! acumulador
# suma = 0
# #! contador
# aprobado = 0


# for i in range(0, 18):
#     # nombre = input('ingrese el nombre del alumno ')
#     nota = float(input("ingrese la nota del alumno"))


#     if(nota >= 6):
#         suma += nota #! suma = suma + nota
#         aprobado += 1 #! aprobado = aprobado + 1
#         print("aprobó la materia")
#     else:
#         print("no aprobó la materia")

# print('el promedio es', suma/aprobado)

# maximo = int(input('ingrese un numero '))

# for i in range(0, 4):
#     numero = int(input('ingrese un numero '))

#     if(numero > maximo):
#         maximo = numero
    

# print('el maximo es', maximo)

positivos = 0
negativos = 0

numero = int(input('ingrese un numero '))

while(numero != 0):
    if(numero > 0):
        positivos += 1
    else:
        negativos += 1
    
    numero = int(input('ingrese un numero '))

print('cantidad de positivos', positivos)
print('cantidad de negativos', negativos)

