
#! FUNCION RETORNA --> 0, 1, MUCHOS

#import mis_funciones

from mis_funciones import suma, agregar

#import mis_funciones as mf


# datos = ['ana', 'juan', 'julieta', 'mariano']

# numero1 = 3
# numero2 = 7
# total = 0
# suma(numero1, numero2, total)

# print('el resultado de la suma es', total)

# agregar(datos, 'hernan')
# print(datos)

# listado(datos)

# print()

# print(datos)
# datos.append('pedro')
# datos.append('maria')
# datos.append('esteban')
# print(datos)

# listado(datos)


from funciones import positivo_negativo


# numero = int(input('ingrese un valor '))

# if(positivo_negativo(numero)):
#     print('algo')
# else:
#     print('otra cosa')
from funciones import contar_caracter, es_palindromo, sumatoria

palabra = "neuquen"

print(contar_caracter(palabra, "m"))

if(es_palindromo(palabra)):
    print('es palindromo')
else:
    print('no es palindromo')


print(sumatoria(6))


#! DICCIONARIOS clave-valor

json = [{'nombre':'walter', 'edad':30},
        {'nombre':'Tito', 'edad':30}, 
        {'nombre':'Ana', 'edad':30}]

for persona in json:
    print(persona['nombre'], persona['edad'])

dic = {13 : 'Julieta'}
print(dic)


key = '144'

dic['14'] = 'Ana'
print(dic)

if(key in dic):
    print(dic[key])
else:
    print('la clave no esta')



lista = [['lunes', 2], ['martes', 3], ['miercoles',0], ['jueves', 10], ['viernes',9]]
        
# for elemento in lista:
#     print(elemento)
#     if(2 in elemento):
#         print(elemento.index(2))
# print()
# for i in range(0, len(lista)):
#     if('lunes' in lista[i]):
#         print(i, lista[i].index('lunes'))
#     # print(lista[i])
#     #print(lista[i].index())

# dic = {1 : 'hola', 2:'chau', 'g' : "algo"}
# clave = 'g'
# if(clave in dic):
#     print(dic[clave])
# print(lista[3])

# print(dic.get('a'))
# print(dic.pop('g'))