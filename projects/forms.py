from dataclasses import field
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','tags','demo_link','source_link','featured_image']