from django import forms
from django.forms.widgets import Widget
from blog import models

class info_form(forms.ModelForm):
    
    user_birth = forms.DateField(widget=forms.TextInput(attrs=({'type':'date'})))

    class Meta:
        model = models.info
        fields = '__all__'
        
class data_form(forms.ModelForm):
    class Meta:
        model = models.data
        fields = '__all__'