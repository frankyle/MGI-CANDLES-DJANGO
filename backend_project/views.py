from django.http import HttpResponse, JsonResponse

# Home view
def home(request):
    return HttpResponse("Welcome to MGI Admin side. Please be responsible and contact the CEO for access to this side.")

# Health check view
def health_check(request):
    return JsonResponse({
        'status': 'OK',
        'message': 'Django backend is reachable.'
    })
