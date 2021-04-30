
import json
import requests


def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
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
            sw_data.append(personaje) #print(doc["name"], doc["url"][28:-1])
        data = get_docs(data["next"])
    
    return sw_data




# print(get_all_sw_characters())
# print(get_charter_by_id(20))
# print(search_characters_by_name('sky'))


# print(result)
# for key in result:
#     print(key, ':', result[key])


#dic = get_docs("https://swapi.dev/api/starships/")
#while(dic["next"] is not None):
#    for doc in dic["results"]:
#        print(doc["name"], doc["url"][31:-1])
#    dic = get_docs(dic["next"])