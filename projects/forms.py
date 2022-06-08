from dataclasses import field
from tkinter.tix import Form
from django import forms
from django.forms import ModelForm, widgets
from .models import Project, Review

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
        

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
    
        labels = {
            'value':'place your vote',
            'body' : 'Add a comment with your vote'
        }
    def __init__(self,*args,**kwrgs):
        super(ReviewForm,self).__init__(*args,**kwrgs)
        
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input'})
        