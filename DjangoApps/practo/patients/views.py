from django.shortcuts import render

# Create your views here.
def patienthome(request):
    return render(request,'patienthome.html')