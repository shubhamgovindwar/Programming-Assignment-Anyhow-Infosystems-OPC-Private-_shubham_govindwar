from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm

class AddInventoryForm(forms.ModelForm):
    class Meta:
        model=InventoryRecord
        fields="__all__"

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
