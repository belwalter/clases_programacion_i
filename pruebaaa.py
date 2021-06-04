

def ordenar_nombre(peronaje):
    return peronaje['name']


def altura(item):
    if(item['height'].isdecimal()):
        return int(item['height'])
    else:
        return 0


def peso(item):
    if(item['mass'].isdecimal()):
        return float(item['mass'])
    else:
        return 0


def color_pelo(item):
    return item['hair_color'] + item['name']


def busqueda(lista, buscado):
    pos = None

    # for i in range(len(lista)):
    #     if(lista[i]['name'] == buscado):
    #         pos = i

    for index, personaje in enumerate(lista):
        if(personaje['name'] == buscado):
            pos = index
    
    return pos

from consumo_api import get_all_sw_characters, get_all_sw_characters_names
from consumo_api import get_planeta_id, search_plantes_by_name
from consumo_api import search_characters_by_name, get_nave, get_charter_by_id, get_film

# sw_data = get_all_sw_characters_names()
sw_data = get_all_sw_characters()

# #! TIMSORT
# sw_data.sort(key=peso)

# buscado = 'R2-D2'

# posicion = busqueda(sw_data, buscado)

# if(posicion is not None):
#     print(buscado, 'esta en la lista en la posicion', posicion)
#     print('info')
#     print(sw_data[posicion]['name'], sw_data[posicion]['species'])
# else:
#     print(buscado, 'no esta en la lista')

tatooine = 'http://swapi.dev/api/planets/1/'
altura_acumulada = 0
peso_huamos = 0
total_humanos = 0
droides = 0

personajes_buscado = False
for personaje in sw_data:
    altura_acumulada += altura(personaje)
    if('http://swapi.dev/api/species/1/' in personaje['species']):
        print('-->', personaje['name'], personaje['mass'])
        peso_huamos += peso(personaje)
        total_humanos += 1
    if('http://swapi.dev/api/species/2/' in personaje['species']):
        droides += 1
    if(personaje['name'][0] in ['C', 'L', 'A']):
        print(personaje['name'])
    # if(personaje['name'] == 'Yoda'):
    #     print(personaje['name'])
    #     print(personaje['species'])
    #     print(personaje['homeworld'])
    #     print(personaje['films'])
    # if(personaje['name'] == 'Grogu' or personaje['name'] == 'Mandalorian'):
    #     personajes_buscado = True
    # if(altura(personaje) < 98):
    #     print(personaje['name'], 'mide menos de 98 cm')
    # if(peso(personaje) > 100):
    #     print(personaje['name'], 'pesa mas de 100 kilos')
    
    # if(personaje['homeworld'] == tatooine):
    #     print(personaje['name'], 'es nativo de Tatooine')
    # if(personaje['homeworld'] == 'http://swapi.dev/api/planets/9/'):
    #     print(personaje['name'], 'es nativo de Coruscant')
    # if('http://swapi.dev/api/species/36/' in personaje['species']):
    #     print(personaje['name'], 'es especie Kaleesh')
    # if('http://swapi.dev/api/species/32/' in personaje['species']):
    #     print(personaje['name'], 'es especie Kaminoan')

print('altua promedio', altura_acumulada/len(sw_data))
print('peso promedio humanos', peso_huamos/total_humanos)
print('cantidad de droides', droides)
# print()
# if(personajes_buscado):
#     print('uno de los personajes esta en la lista')
# else:
#     print('ninguno de los personajes estan')

# print(get_planeta_id(9))
# print()
# print(search_plantes_by_name('Kamino'))

# luke = search_characters_by_name('Anakin Skywalker')[0]

# for nave_url in luke['starships']:
#     print(get_nave(nave_url))

# r2d2 = search_characters_by_name('R2-D2')[0]

# for peli_url in r2d2['films']:
#     print(get_film(peli_url)['title'])

# new_hope = get_film('https://swapi.dev/api/films/1/')
# print(new_hope['opening_crawl'])

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

#! Calcular el promedio de altura de todos los personajes (acumulador)
#! Calcular el peso promedio de los personajes especie humanos (acumulador, contar)
#! Contar cuantos personajes especie droides y humanos (contador)
#! Listar todos los personajes que comienzan con C, L, A 