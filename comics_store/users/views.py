# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from users.models import User

from django.http import JsonResponse
from rest_framework.authtoken.models import Token
import datetime

import json
import base64

def login_user(request):
    if request.method == 'POST':
        body_decoded = request.body.decode()
        body_dict = json.loads(body_decoded)

        print(body_dict)
        
        username_encoded = body_dict["username"]
        name_encoded = body_dict["name"]
        age_encoded = body_dict["age"]
        password_encoded = body_dict["password"]

        user_data = dict({
            'username' : base64.b64decode(username_encoded).decode(),
            'name' : base64.b64decode(name_encoded).decode(),
            'age' : base64.b64decode(age_encoded).decode(),
            'password' : base64.b64decode(password_encoded).decode()
            })

        print(user_data)

        # username_plain = base64.b64decode(username_encoded).decode()

        # user = User.objects.get(username=username_plain)

        # user = User.objects.get(username=username_plain)

        # token = Token.objects.create(username=user)
        # print(token.key)


        # print(type(body_dict))

        default_response = {
            'status': 0, 
            'errors': [],
            'message': 'Datos Recibidos. Probando internamente las operaciones.', 
            'opsDate': datetime.datetime.now()
        }

        return JsonResponse(default_response)
        


# import base64

# data = "abc123!?$*&()'-=@~"

# # Standard Base64 Encoding
# encodedBytes = base64.b64encode(data.encode("utf-8"))
# encodedStr = str(encodedBytes, "utf-8")

####################################################################################
# GENERADOR DE JSON WEB TOKENS:
#
# from rest_framework_jwt.settings import api_settings
#
# if request.method == 'POST':
#     jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#     jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#     payload = jwt_payload_handler(request.user)
#     token = jwt_encode_handler(payload)
#     return HttpResponse('Get token auth request and data is as: {}'.format(token))
#
# CON TRY, EXCEPT SERÍA:
# def jwt_encode(user):
#     try:
#         from rest_framework_jwt.settings import api_settings
#     except ImportError:
#         raise ImportError("djangorestframework_jwt needs to be installed")

#     jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#     jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#     payload = jwt_payload_handler(user)
#     return jwt_encode_handler(payload) 
#
#
# OTRO EJEMPLO:
#
#
# def generate_jwt_token(user, data):
#     jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#     jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#     payload = jwt_payload_handler(user)
#     token = jwt_encode_handler(payload)
#     data['token'] = token
#     return data 
####################################################################################




#     # username = request.POST['username']
    #     # password = request.POST['password']
    #     # user = authenticate(request, username=username, password=password)
    #     # if user is not None:
    #     #     login(request, user)
    #     #     # Redirect to a success page.
    #     #     return "login success"
    #     # else:
    #     #     # messages.success(request, "Hay un error en tu autenticación, intenta de nuevo.")
    #     #     # # Return an invalid error message.
    #     #     # # response.satus_code(401)
    #     #     return "Else fail login"
    #     return JsonResponse({'message': 'Tú muy bien'})
    # else:
    #     return "Else..."