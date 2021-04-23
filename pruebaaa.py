
from funciones import calculadora, es_vocal



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



from consumo_api import get_data_sw_characters

sw_data = get_data_sw_characters()

# #! TIMSORT
sw_data.sort(key=peso)

for index, character in enumerate(sw_data):
    print(character['name'], character['height'], character['mass'])
