
from consumo_api import get_charter_by_id, get_all_sw_characters
from random import randint

# 1
# def altura(item):
#     if(item['height'].isdecimal()):
#         return int(item['height'])
#     else:
#         return 0


# def peso(item):
#     if(item['mass'].isdecimal()):
#         return float(item['mass'])
#     else:
#         return 0


# id_1 = randint(1, 83)
# id_2 = randint(1, 83)

# personaje1 = get_charter_by_id(id_1)
# personaje2 = get_charter_by_id(id_2)

# print(personaje1['name'], personaje2['name'])

# # A
# print('altura')
# if(altura(personaje1) > altura(personaje2)):
#     print(personaje1['name'])
# else:
#     print(personaje2['name'])

# # B
# print('peso')
# if(peso(personaje1) > peso(personaje2)):
#     print(personaje1['name'])
# else:
#     print(personaje2['name'])

# # C
# print('peliculas')
# if(len(personaje1['films']) > len(personaje2['films'])):
#     print(personaje1['name'])
# elif(len(personaje2['films']) > len(personaje1['films'])):
#     print(personaje2['name'])
# else:
#     print(personaje1['name'], personaje2['name'])

# # D
# print('nombres')
# if(personaje1['name'] == "Yoda" or personaje1['name'] == "Grevious"):
#     print('personaje 1', personaje1['name'])
# if(personaje2['name'] == "Yoda" or personaje2['name'] == "Grevious"):
#     print('personaje 2', personaje2['name'])

# def nombre(item):
#     return item['name']

# # 2


# personajes = get_all_sw_characters()

# personajes.sort(key=nombre)

# for personaje in personajes:
#     print(personaje['name'], personaje['species'], personaje['homeworld'])
#     if(len(personaje['films']) == 6):
#         print('participo en todas las peliculas')

# 3
# lista = []

# for i in range(77):
#     lista.append(randint(1, 100))

# lista.sort()

# print('menor', lista[0])
# print('mayor', lista[-1])

# print('listado')
# for num in lista:
#     print(num)

# print('listado pares')
# for num in lista:
#     if(num % 2 == 0):
#         print(num)
