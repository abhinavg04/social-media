from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView
from django.views import View
from .forms import UserInfo
from .models import Profile,Post
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

def search_profile(request):
    searched = request.GET.get('searched')
    users = User.objects.filter(username__contains = searched)
    return render(request,'search.html',{'users':users})
    

#add like view
def add_like(request,id):
    post = Post.objects.get(id=id)
    if post.likes.filter(id=request.user.profile.id):
        post.likes.remove(request.user.profile)
    else:
        post.likes.add(request.user.profile)
    return redirect('userhome')
class ProfileList(ListView):
    template_name='profile_list.html'
    queryset=Profile.objects.all()
    context_object_name='profiles'
    def get_queryset(self):
        resp = super().get_queryset()
        resp = resp.filter(~Q(user=self.request.user) & ~Q(user__is_superuser=True))
        return resp

def upload(request):
    if request.method == 'POST':
        userprofile = Profile.objects.get(user=request.user)
        if request.FILES.get('video'):
            video = request.FILES['video']
        else:
            video = None
        if request.FILES.get('image'):
            image = request.FILES['image']
        else:
            image = None
        caption = request.POST.get('caption')
        new_post = Post(userprofile=userprofile,image=image,video = video,caption=caption)
        new_post.save()
        return redirect('userhome')
    else:
        return redirect('userhome')

class UserPage(TemplateView):
    template_name='user_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by('-created_at')
        context['profiles'] = Profile.objects.filter(~Q(user=self.request.user) & ~Q(user__is_superuser = True))
        return context
    

class ProfilePage(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            profile = Profile.objects.get(id=id)
            posts = Post.objects.filter(userprofile=profile)
            return render(request,'profile.html',{'profile':profile,'posts':posts})
        else:
            messages.error(request,'Loggin to view this page')
            return redirect('userhome')
    def post(self,request,id):
        profile = Profile.objects.get(id=id)
        if request.user.is_authenticated:
            current_user_profile = request.user.profile
            action = request.POST.get('follow')
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            else:
                current_user_profile.follows.add(profile)
            current_user_profile.save()
        return redirect('profile',id)

    


class EditProfile(View):
    def get(self,request,id):
        current_profile = Profile.objects.get(id=id)
        form = UserInfo(instance=current_profile)
        return render(request,'edit_profile.html',{'form':form })
    def post(self,request,id):
        current_profile = Profile.objects.get(id=id)
        form = UserInfo(data=request.POST,files=request.FILES,instance=current_profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Edited')
            return redirect('profile',id)
        else:
            return render(request,'edit_profile.html',{'form':form })
