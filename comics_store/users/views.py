from django.shortcuts import render

# Create your views here.


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