from django.urls import path, include
from .views import CountryView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('countries', CountryView)

app_name = 'locations_api'
urlpatterns = [
    path('', include(router.urls)),
]