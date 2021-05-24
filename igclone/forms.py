from django import forms
from .models import Image,Comment,Profile

class NewImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','user_profile','likes']