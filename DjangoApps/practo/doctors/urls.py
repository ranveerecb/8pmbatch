from django.urls import path
from .views import doctorhome
urlpatterns = [
    path('doctor/',doctorhome,name= 'doctorl')
]
