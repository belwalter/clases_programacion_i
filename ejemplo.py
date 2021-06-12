from consumo_api import get_charter_by_id, get_docs, get_specie


people = get_charter_by_id(13) # 79


class Specie(object):

    def __init__(self, name, language, classification):
        self.__name = name
        self.__language = language
        self.__classification = classification

    def __str__(self):
        return self.__name 


class Planet(object):

    def __init__(self, name, climate, diameter=None):
        self.__name = name
        self.__climate = climate
        self.__diameter = diameter
    
    def planet_info(self):
        print(self.__name, self.__climate, self.__diameter)

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return self.__name
    

class People(object):

    def __init__(self, name, specie, homeworld=None):
        self.__name = name
        self.__specie = specie
        self.__homeworld = homeworld
    
    @property
    def homeworld(self):
        return self.__homeworld
    
    @homeworld.setter
    def homeworld(self, homeworld):
        if(isinstance(homeworld, Planet)):
            self.__homeworld = homeworld
        else:
            print('el homeworld debe ser un objeto planet')

    @property
    def specie(self):
        return self.__specie

    def print_info(self):
        print(self.__name, self.__specie, self.__homeworld)


planet1_api = get_docs(people['homeworld'])
planet = Planet(planet1_api['name'], planet1_api['climate'], planet1_api['diameter'])
specie1_api = get_specie(people['species'][0])
specie = Specie(specie1_api['name'], specie1_api['language'], specie1_api['classification'])

personaje = People(people['name'], specie, planet)
# personaje.homeworld = planet

# planet.planet_info()
personaje.print_info()

# personaje.homeworld.planet_info()
# personaje.specie.specie_info()

print(personaje.specie)
print(personaje.homeworld)
