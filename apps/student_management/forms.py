from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'current_academic_level',
            'enrollment_status',
            'photo',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Name'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'gender': forms.RadioSelect(
                choices= Student.GENDER_CHOICES,
                attrs= {'class': 'custom-radio-buttons'}
            ),
            'current_academic_level': forms.Select(
                choices= Student.CURRENT_LEVEL_CHOICES,
                attrs= {'class': 'form-select'}
            ),
            'enrollment_status': forms.Select(
                choices= Student.ENROLLMENT_STATUS_CHOICES,
                attrs= {'class': 'form-select'}
            ),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            
        }