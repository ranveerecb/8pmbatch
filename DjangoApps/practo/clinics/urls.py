from django.urls import path
from .views import clinichome
urlpatterns = [
    path('',clinichome),
    path('home/',clinichome,name='clinicl')
]
