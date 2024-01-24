from django.urls import path
from django.conf.urls import include
from .views import getGOAuthToken

urlpatterns = [
  path('login/google-oauth',getGOAuthToken )
]
