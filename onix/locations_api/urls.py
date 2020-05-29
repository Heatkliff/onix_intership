from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'cities', views.CityViewSet)

app_name = 'locations_api'
urlpatterns = [
    re_path(r'countries/(?P<country_id>[0-9]+)$',  # Url to get update or delete a movie
            views.CountryApiView.as_view(),
            name='CountryApiView'
            ),
    path('countries/',  # urls list all and create new one
         views.CountriesApiView.as_view(),
         name='CountriesApiView'
         ),
    path('', include(router.urls)),
]
