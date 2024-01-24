from django.urls import path
from django.conf.urls import include


urlpatterns = [
  path('gauth/', include('gauth.api_urls')),
]

