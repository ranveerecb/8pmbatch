from django.urls import path,include

urlpatterns = [
    path('', include('clinics.urls')),
    path('', include('doctors.urls')),
    path('', include('patients.urls'))
]
