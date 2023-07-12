from django.urls import path, include
from rest_framework import routers

from holder.views import StatisticViewSet

router = routers.DefaultRouter()
router.register(r'message', StatisticViewSet, basename='message')


urlpatterns = [
    path('', include(router.urls)),
]