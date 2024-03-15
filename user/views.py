from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class UserPage(TemplateView):
    template_name='user_page.html'
