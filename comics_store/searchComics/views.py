from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# import asyncio
import requests

def index(request):
    
    response = requests.get('https://gateway.marvel.com/v1/public/comics?ts=1&apikey=6b458513b5383de9cf55d82c26551dd1&hash=eb6f264d37e1fd74ad010baa8b900005')
    data_set = response.json()

    return JsonResponse(data_set)