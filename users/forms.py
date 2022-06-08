from email import message
from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill,Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email', 'username','password1','password2']
    
    def __init__(self,*args,**kwrgs):
        super(CustomUserCreationForm,self).__init__(*args,**kwrgs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','location','bio','short_intro','profile_image','social_github','social_linkedin','social_youtube','social_website','social_twitter']

    def __init__(self,*args,**kwrgs):
        super(ProfileForm,self).__init__(*args,**kwrgs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude=['owner']

    def __init__(self,*args,**kwrgs):
        super(SkillForm,self).__init__(*args,**kwrgs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})




class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']

    def __init__(self,*args,**kwrgs):
        super(MessageForm,self).__init__(*args,**kwrgs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})