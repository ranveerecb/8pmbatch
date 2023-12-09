from django.http import HttpResponse

def home(request):
    text='<h1>Welcome to Django first Application'
    return HttpResponse(text)