from django.shortcuts import render
from django.http import JsonResponse

from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")

def home(request):
    context = {
        'client_id': CLIENT_ID,  # Replace with your client_id
        'redirect_uri': REDIRECT_URI,  # Replace with your redirect_uri
    }
    return render(request, 'home.html', context)



# def auth(request):
#     full_url = request.build_absolute_uri()
#     base_url = request.build_absolute_uri('/')[:-1].strip("/")
#     parsed_url = urlparse(full_url)
#     parameters = parse_qs(parsed_url.query)

#     context = {
#         'full_url': full_url,
#         'base_url': base_url,
#         'parameters': parameters,
#     }
#     return render(request, 'auth.html', context)


import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs

load_dotenv()  # take environment variables from .env.

def auth(request):
    full_url = request.build_absolute_uri()
    base_url = request.build_absolute_uri('/')[:-1].strip("/")
    parsed_url = urlparse(full_url)
    parameters = parse_qs(parsed_url.query)
    code = parameters.get('code', [''])[0]  # extract the code

    context = {
        'full_url': full_url,
        'base_url': base_url,
        'parameters': parameters,
    }

    # Exchange the code for a token
    if code:
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")
        redirect_uri = os.getenv("REDIRECT_URI")

        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': code,
        }

        try:
            response = requests.post('https://api.instagram.com/oauth/access_token', data=data)
            response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx

            # If the request is successful, no Exception will be raised
            context['token_response'] = response.json()
        except requests.exceptions.HTTPError as errh:
            context['error'] = f"Http Error: {errh}"
        except requests.exceptions.ConnectionError as errc:
            context['error'] = f"Error Connecting: {errc}"
        except requests.exceptions.Timeout as errt:
            context['error'] = f"Timeout Error: {errt}"
        except requests.exceptions.RequestException as err:
            context['error'] = f"Oops: Something Else: {err}"
    else:
        context['erro']= "Invalid-request: No code fount"
    return render(request, 'auth.html', context)
