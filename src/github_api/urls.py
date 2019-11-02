from django.urls import path, include
from .views import *


urlpatterns = [
    path('', github_client, name='github')
]
