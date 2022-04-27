### Pending
# It's better a Class, Doesn't?
#
# import requests

# class GetJson(self, url_api):
#     def __init__(self):
#         self.url_api = url_api
###
import json

# Returns a Python Dictionary for more dynammism.
def getJson_characters(api_data):

    print(api_data)

    data_results = api_data.get('results')

    lista_personajes = []

    for personaje in range(len(data_results)):
        
        id = data_results[personaje].get('id')
        name = data_results[personaje].get('name')
        image = str(data_results[personaje].get('thumbnail').get('path')) + "." + str(data_results[personaje].get('thumbnail').get('extension'))
        appearances = data_results[personaje].get('comics').get('available')

        payload = {"id": id, "name": name, "image": image, "appearances": appearances}

        lista_personajes.append(payload)

    def orderByName(e):
        return e['name']

    lista_personajes.sort(key=orderByName)

    return lista_personajes


def getJson_comics(api_data):

    data_results = api_data.get('results')

    lista_comics = []

    for comic in range(len(data_results)):
        
        id = data_results[comic].get('id')
        title = data_results[comic].get('title')
        image = str(data_results[comic].get('thumbnail').get('path')) + "." + str(data_results[comic].get('thumbnail').get('extension'))
        dates = data_results[comic].get('dates')
        onsaleDate = dates[0].get('date')

        payload = {"id": id, "title": title, "image": image, "onsaleDate": onsaleDate}
        
        lista_comics.append(payload)

    return lista_comics
