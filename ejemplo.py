from consumo_api import get_charter_by_id, get_docs


people = get_charter_by_id(79)


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
        self.__homeworld = homeworld

    def print_info(self):
        print(self.__name, self.__specie, self.__homeworld.name)


planet1_api = get_docs(people['homeworld'])

planet = Planet(planet1_api['name'], planet1_api['climate'], planet1_api['diameter'])

personaje = People(people['name'], get_docs(people['species'][0])['name'], planet)

# planet.planet_info()
# personaje.print_info()

personaje.homeworld.planet_info()

#! class specie