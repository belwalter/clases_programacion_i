
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

json = [{'nombre':'walter', 'edad':30},{'nombre':'Tito', 'edad':30}, {'nombre':'Ana', 'edad':30}]

for persona in json:
    print(persona['nombre'], persona['edad'])

dic = {}
print(dic)

dic['14'] = 'Ana'
print(dic)