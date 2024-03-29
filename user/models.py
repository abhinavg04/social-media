from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='')
    phone = models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=100, blank=True)
    follows = models.ManyToManyField('self',
                                     related_name='followed_by',
                                     symmetrical=False,blank=True)
    def __str__(self):
        return self.user.username
    
#create user profile by default
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile  = Profile(user = instance)
        user_profile.save()
#automate profile creation
post_save.connect(create_profile,sender=User)

    

class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    userprofile = models.ForeignKey(Profile,on_delete=models.DO_NOTHING,related_name = 'userpost')
    video = models.FileField(upload_to='video',null=True)
    image = models.ImageField(upload_to='post_images',null=True)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Profile,related_name='post_like',blank=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.userprofile.user.username
