from django.urls import path
from . views import *
urlpatterns = [
    path('',Reg.as_view(),name='reg'),
    path('logout',logout_user,name='logout'),
    path('update_user/',update_user,name='update_user'),
    path('update_pswd/',UpdatePassword.as_view(),name='update_pswd'),
]