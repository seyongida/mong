from django.forms import ModelForm
from .models import *


class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content', 'writer']
        
class BoardForm2(ModelForm):
    class Meta:
        model = Board2
        fields = ['title', 'content']
        
class BoardForm3(ModelForm):
    class Meta:
        model = Board3
        fields = ['title', 'content', 'imgfile']