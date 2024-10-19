# views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to MGI Admin side, Can you please be a Responsible person and Contact the CEO for access to this side")
