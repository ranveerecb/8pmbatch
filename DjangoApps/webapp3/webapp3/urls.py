from django.urls import path,include

urlpatterns = [
    path('', include('myapp1.urls')),
]
