from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views
from .drf import schema_view

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
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('re-token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.CreateUserAPIView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('google_login/', views.GoogleView.as_view(), name='google'),  # add path for google authentication
]
