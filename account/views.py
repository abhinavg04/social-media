from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,FormView,CreateView
from . forms import RegForm,LoginForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

class Landing(FormView):
    form_class=LoginForm
    template_name = 'landing.html'
    def post(self,request):
        form_data = LoginForm(data=request.POST)
        if form_data.is_valid():
            uname = form_data.cleaned_data.get('username')
            pswd = form_data.cleaned_data.get('password')
            user = authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,'Login Successfull')
                return redirect('userhome')
            else:
                messages.error(request,'Login Failed')
                return redirect('login')
        else:
            return render(request,'login.html',{'form':form_data})


class Reg(View):
    def get(self,request):
        regform = RegForm()
        return render(request,'reg.html',{'form':regform})
    def post(self,request):
        form_data = RegForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Signup Successfull')
            return redirect('landing')
        else:
            messages.error(request,'Registration Failed')
            return redirect('landing')   

# class LoginView(FormView):
#     form_class=LoginForm
#     template_name='login.html'
    