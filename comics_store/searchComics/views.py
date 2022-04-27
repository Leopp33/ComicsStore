import json
import requests
from django.http import HttpResponse

from modules.getApiData import getJson_characters, getJson_comics

characters_url = 'https://gateway.marvel.com/v1/public/characters?ts=1&apikey=6b458513b5383de9cf55d82c26551dd1&hash=eb6f264d37e1fd74ad010baa8b900005' 
comics_url = 'https://gateway.marvel.com/v1/public/comics?ts=1&apikey=6b458513b5383de9cf55d82c26551dd1&hash=eb6f264d37e1fd74ad010baa8b900005'
'https://gateway.marvel.com/v1/public/comics?ts=1&apikey=6b458513b5383de9cf55d82c26551dd1&hash=eb6f264d37e1fd74ad010baa8b900005'

def index(request):

    if request.GET:
        
        request_params = json.dumps(request.GET)
        req_dict = json.loads(request_params)
        
        keys_output = []
        name_key = [x for x in req_dict if x == 'name']
        title_key = [x for x in req_dict if x == 'title']
        keys_output.append(name_key)
        keys_output.append(title_key)

        if str(keys_output[0]) == "['name']":
            # Make a request to Marvel API.
            apiRequest = requests.get(characters_url)
            # Get the JSON one. 
            apiResponse = apiRequest.json()
            # Access to the data property.
            content = apiResponse['data']

            # Receive the Python Dictionary parsed.
            data_characters = getJson_characters(content)

            data_set = json.dumps(data_characters, indent=4)

        elif str(title_key) == "['title']":
            # Make a request to Marvel API.
            apiRequest = requests.get(comics_url)
            # Get the JSON one. 
            apiResponse = apiRequest.json()
            # Access to the data property.
            content = apiResponse['data']
            # Receive the Python Dictionary parsed.
            data_comics = getJson_comics(content)

            data_set = json.dumps(data_comics, indent=4)
                
    else:
        # Make a request to Marvel API.
        apiRequest = requests.get(characters_url)
        # Get the JSON one. 
        apiResponse = apiRequest.json()
        # Access to the data property.
        content = apiResponse['data']

        # Receive the Python Dictionary parsed.
        data_characters = getJson_characters(content)
        # Default Resuls: By Name
        data_set = json.dumps(data_characters, indent=4)
        # data_set = json.dumps({'message': 'else: principal'})

    # Return to View/Consumer a JSON formated response.
    return HttpResponse(data_set, content_type="application/json")