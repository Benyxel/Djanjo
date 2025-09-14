from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hones_Views, name='honesviews' )
]