from django.urls import path
from . import views

urlpatterns = [
    path('', views.Account_View, name='account_views' )
]