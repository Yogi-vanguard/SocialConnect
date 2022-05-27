from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email', 'username','password1','password2']
    
    def __init__(self,*args,**kwrgs):
        super(CustomUserCreationForm,self).__init__(*args,**kwrgs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input'})