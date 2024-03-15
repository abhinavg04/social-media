from django.urls import path
from . views import *
urlpatterns = [
    path('',Reg.as_view(),name='reg'),
]