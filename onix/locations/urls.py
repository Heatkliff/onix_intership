from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country/<int:country_id>', views.single_country, name='single_country'),
    path('cities/<int:city_id>', views.single_city, name='single_country'),
    path('cities/<int:city_id>/delete', views.delete_city, name='single_country'),
]
