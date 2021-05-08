

def ordenar_nombre(peronaje):
    return peronaje['name']

def altura(item):
    # print(item, type(item))
    if(item['height'].isdecimal()):
        return int(item['height'])
    else:
        return -1

def peso(item):
    if(item['mass'].isdecimal()):
        return float(item['mass'])
    else:
        return -1

def color_pelo(item):
    return item['hair_color'] + item['name']

def busqueda(lista, buscado):
    pos = -1

    # for i in range(len(lista)):
    #     if(lista[i]['name'] == buscado):
    #         pos = i

    for index, personaje in enumerate(lista):
        if(personaje['name'] == buscado):
            pos = index
    
    return pos

from consumo_api import get_all_sw_characters, get_all_sw_characters_names

# sw_data = get_all_sw_characters_names()
# sw_data = get_all_sw_characters()

# #! TIMSORT
# sw_data.sort(key=peso)

# buscado = 'Yoda'

# posicion = busqueda(sw_data, buscado)

# if(posicion > -1):
#     print(buscado, 'esta en la lista en la posicion', posicion)
#     # sw_data[posicion]['species'] = "desconosido"
#     print('info')
#     print(sw_data[posicion])
#     # sw_data.pop(posicion)
# else:
#     print(buscado, 'no esta en la lista')



# for character in sw_data:
#     if(character['mass'].isdecimal()):
#         if(int(character['mass']) >= 100):
#             print(character['name'], character['mass'])
    
    # print(character['name'])
    # print(character['name'], character['height'], character['mass'])



#! Mostrar toda la informacion de Yoda si esta en la Lista
#! Determinar si Mandalorian o Grogu esta en la lista
#! Mostrar todos los personajes con altura menor a 98 cm
#! Mostrar todos los personajes con peso mayor a 100 kilos
#! Mostrar todos los personajes del planeta natal Tatooine y Coruscant
#! Mostrar todos los personajes de especie Kaleesh y Kaminoan

#! Mostrar toda la informacion del planeta Coruscant y Kamino
#! Mostrar toda la informacion de las naves usadas por Luke Skywalker
#! Mostarr toda las peliculas en las que aparecio R2-D2
#! Mostrar el resumen de la introduccion (opening_crawl) del episodio 4 "A New Hope"   
 
#! Calcular el promedio de altura de todos los personajes
#! Calcular el peso promedio de los personajes especie humanos
#! Contar cuantos personajes especie droides y humanos hay
#! Listar todos los personajes que comienzan con C, L, A

from consumo_api import get_all_sw_characters, get_charter_by_id

sw_data = get_all_sw_characters()

# for personaje in lista_personajes:
    
#     print(personaje)

for character in sw_data:

    if ("http://swapi.dev/api/species/32/" in character['species']):
        print(character ["name"], character["species"])
    elif ("http://swapi.dev/api/species/36/" in character['species']):
        print(character ["name"], character["species"]) 

# personaje = get_charter_by_id(20)
# print(personaje)