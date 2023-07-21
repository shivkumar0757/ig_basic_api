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



def auth(request):
    full_url = request.build_absolute_uri()
    base_url = request.build_absolute_uri('/')[:-1].strip("/")
    parsed_url = urlparse(full_url)
    parameters = parse_qs(parsed_url.query)

    context = {
        'full_url': full_url,
        'base_url': base_url,
        'parameters': parameters,
    }
    return render(request, 'auth.html', context)

