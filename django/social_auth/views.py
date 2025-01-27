
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.conf import settings
from urllib.parse import urlencode
import requests
import json

def index(request):
    return HttpResponse(
        "<h1>This is my index page. Welcome, human.</h1>"
        "<a href='/login/google/'>Login with Google</a>"
    )

def google_login(request):
    params = {
        'scope': 'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile',
        'access_type': 'offline',
        'response_type': 'code',
        'redirect_uri': 'http://localhost:8000/social-auth/callback/google/',
        'prompt': 'consent',
        'include_granted_scopes': 'true',
        'client_id': settings.GOOGLE_CLIENT_ID,
    }

    url = settings.GOOGLE_OAUTH_ENDPOINT + '?' + urlencode(params)
    return HttpResponseRedirect(url)

def google_callback(request):
    if 'code' in request.GET:
        code = request.GET.get('code')
        data = {
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'code': code,
            'redirect_uri': 'http://localhost:8000/social-auth/callback/google/',
            'grant_type': 'authorization_code',
        }
        url = settings.GOOGLE_AUTHORIZATION_CODE_ENDPOINT
        response = requests.post(url, data=data)

        if not hasattr(response, 'json'): return HttpResponse(response.content)

        access_token = response.json().get('access_token')
        print(json.dumps(response.json()))

        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(settings.GOOGLE_USERINFO_ENDPOINT, headers=headers)

        if not hasattr(response, 'json'): return HttpResponse(response.content)

        user_data = response.json()
        s = ''
        for key_value in [f'<b>{key}</b> : {user_data[key]}' for key in user_data]: s += '<li>' + key_value + '</li>'
        return HttpResponse(
            "<h2>Google Login Successful!🎉</h2>"
            "<p><b>User credentials</b></p>"
            "<ul>" + s + "</ul>"
            "<a href='/'>Home</a>"
        )

    elif 'error' in request.GET:
        return HttpResponse(f"<h2>Google Login Unsuccessful.😑</h2><a href='/'>Home</a>")

    else:
        print(request.POST)
        return HttpResponse(f"{request.POST}<a href='/'>Home</a>")

    
"""
https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A//www.googleapis.com/auth/drive.metadata.readonly%20https%3A//www.googleapis.com/auth/calendar.readonly&state=state_parameter_passthrough_value&redirect_uri=https%3A//oauth2.example.com/code&access_type=offline&response_type=code&client_id=583306224539-atbcaa8ne8g85e8kc006o6vmq99qiid0.apps.googleusercontent.com
"""
