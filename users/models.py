from email.policy import default
from re import T
import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    short_intro = models.CharField(max_length=1000,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to="profiles/",default ='profiles/user-default.png')
    social_github = models.CharField(max_length=200,blank=True,null=True)
    nsocial_twitter = models.CharField(max_length=200,blank=True,null=True)
    social_linkedin = models.CharField(max_length=200,blank=True,null=True)
    social_website = models.CharField(max_length=200,blank=True,null=True)
    social_youtube = models.CharField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)

    def __str__(self):
        return str(self.user.username)