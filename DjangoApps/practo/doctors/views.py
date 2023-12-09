from django.shortcuts import render

# Create your views here.
def doctorhome(request):
    return render(request,'doctorhome.html')