from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the ml index.")
    
def classify(request):
    return JsonResponse({'status': 'Classifying...'})