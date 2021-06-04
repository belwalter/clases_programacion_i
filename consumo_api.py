
import requests


def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = req.json()
        return dic


def get_charter_by_id(id):
    data = get_docs("https://swapi.dev/api/people/"+str(id))
    return data


def search_characters_by_name(name):
    data = get_docs("https://swapi.dev/api/people?search="+str(name))
    return data['results']


def get_all_sw_characters():

    sw_data = []

    data = get_docs("https://swapi.dev/api/people/")

    while(data["next"] is not None):
        for personaje in data["results"]:
            sw_data.append(personaje)  # print(doc["name"], doc["url"][28:-1])
        data = get_docs(data["next"])

    return sw_data


def get_all_sw_characters_names():

    sw_data = []

    data = get_docs("https://swapi.dev/api/people/")

    while(data["next"] is not None):
        for personaje in data["results"]:
            # print(doc["name"], doc["url"][28:-1])
            sw_data.append(personaje['name'])
        data = get_docs(data["next"])

    return sw_data


def get_planeta_id(id):
    data = get_docs("https://swapi.dev/api/planets/"+str(id))
    return data


def search_plantes_by_name(name):
    data = get_docs("https://swapi.dev/api/planets?search="+str(name))
    return data['results']


def get_nave(url):
    data = get_docs(url)
    return data

def get_film(url):
    data = get_docs(url)
    return data
