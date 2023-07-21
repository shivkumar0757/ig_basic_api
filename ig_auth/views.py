from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    context = {
        'client_id': '684477648739411',  # Replace with your client_id
        'redirect_uri': 'https://socialsizzle.herokuapp.com/auth/',  # Replace with your redirect_uri
    }
    return render(request, 'home.html', context)


from urllib.parse import urlparse, parse_qs

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


# def auth(request):
#     full_url = request.build_absolute_uri()
#     base_url = request.build_absolute_uri('/')[:-1].strip("/")
#     code = request.GET.get('code', '')

#     data = {
#         'full_url': full_url,
#         'base_url': base_url,
#         'parameters': {
#             'code': code,
#         },
#     }
#     return JsonResponse(data, json_dumps_params={'indent': 2})
