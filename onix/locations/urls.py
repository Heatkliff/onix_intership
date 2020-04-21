from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('static_link/', views.static_link, name='static_link'),
    path('dynamic/<variable>', views.dynamic, name='dynamic'),
    path('media_picture', views.media_picture, name='media_picture'),
    path('bootstrap_link', views.bootstrap_link, name='bootstrap_link'),
]
