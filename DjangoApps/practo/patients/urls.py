from django.urls import path
from .views import  patienthome
urlpatterns = [
    path('patient/',patienthome,name='patientl')
]
