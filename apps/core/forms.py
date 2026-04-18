from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FacultySignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text="Enter your legal first and last name.")
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('full_name', 'email', 'phone_number')