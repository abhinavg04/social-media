from .models import Profile

def userinfo(request):
    if request.user.is_authenticated:
        userinfo = Profile.objects.get(user=request.user)
        return {'userinfo':userinfo}
    else:
        return {'userinfo':''}
