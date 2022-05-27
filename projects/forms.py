from dataclasses import field
from django import forms
from django.forms import ModelForm, widgets
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','tags','demo_link','source_link','featured_image']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self,*args,**kwrgs):
        super(ProjectForm,self).__init__(*args,**kwrgs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input'})
        
