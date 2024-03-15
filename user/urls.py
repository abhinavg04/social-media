from django.urls import path
from . views import *
urlpatterns = [
    path('',UserPage.as_view(),name='userhome'),
]