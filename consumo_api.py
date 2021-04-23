
import json
import requests

#sw_data = []


def get_personajes(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic


result = get_personajes("https://swapi.dev/api/people/190")


for key in result:
    print(key, ':', result[key])


# while(result["next"] is not None):
#     for doc in result["results"]:
#         sw_data.append(doc) #print(doc["name"], doc["url"][28:-1])
#     result = get_docs(result["next"])

# for index, character in enumerate(sw_data):
#     print(index)
#     print(character)
#dic = get_docs("https://swapi.dev/api/starships/")
#while(dic["next"] is not None):
#    for doc in dic["results"]:
#        print(doc["name"], doc["url"][31:-1])
#    dic = get_docs(dic["next"])