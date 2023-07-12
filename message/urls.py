from django.urls import path, include

urlpatterns = [
    path('', include('holder.urls')),
]