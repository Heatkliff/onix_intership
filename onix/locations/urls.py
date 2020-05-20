from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cities/create/', views.create_city, name='create_city'),
    path('country/create/', views.create_country, name='create_country'),
    path('country/<int:country_id>', views.single_country, name='single_country'),
    path('cities/<int:city_id>', views.single_city, name='single_city'),
    path('cities/<int:city_id>/update/', views.update_city, name='update_city'),
    path('country/<int:country_id>/update/', views.update_country, name='update_country'),
    path('cities/<int:city_id>/delete', views.delete_city, name='delete_city'),
]

