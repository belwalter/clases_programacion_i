
import json
import requests


def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic


def get_data_sw_characters():

    sw_data = []

    result = get_docs("https://swapi.dev/api/people/")
    while(result["next"] is not None):
        for doc in result["results"]:
            # print(doc['name'])
            sw_data.append(doc) #print(doc["name"], doc["url"][28:-1])
        result = get_docs(result["next"])
    
    return sw_data







# print(result)
# for key in result:
#     print(key, ':', result[key])


#dic = get_docs("https://swapi.dev/api/starships/")
#while(dic["next"] is not None):
#    for doc in dic["results"]:
#        print(doc["name"], doc["url"][31:-1])
#    dic = get_docs(dic["next"])