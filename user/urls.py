from django.urls import path
from . views import *
urlpatterns = [
    path('',UserPage.as_view(),name='userhome'),
    path('profile/<int:id>',ProfilePage.as_view(),name='profile'),
    path('edit_profile/<int:id>',EditProfile.as_view(),name='editpro'),
    path('upload/',upload,name='upload'),
    path('find_profile/',ProfileList.as_view(),name='find_profile'),
    path('add_like/<id>',add_like,name='add_like'),
    path('search_users/',search_profile,name='search_profile'),
]