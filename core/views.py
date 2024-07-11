from django.shortcuts import render
from django.contrib.sessions.models import Session

def chat(request):
    if not request.session.session_key:
        request.session.create()
    
    return render(request, 'chat.html')
