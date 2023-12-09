from django.shortcuts import render

# Create your views here.
def clinichome(request):
    return render(request,'clinichome.html')