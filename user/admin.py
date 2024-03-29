from django.contrib import admin
from .models import Profile,Post
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)

#mix user info and profile
class ProfileInline(admin.StackedInline):
    model= Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields =['username','first_name','last_name','email']
    inlines=[ProfileInline]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
