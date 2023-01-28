




from dataclasses import fields
from django import forms

from accounts.models import CustomUser, Profile

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from accounts.validators import LowercaseValidator, SpecialCharValidator, UppercaseValidator

from django.contrib.auth.password_validation import validate_password

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password',validators=[validate_password],
    widget=forms.PasswordInput(attrs={'class':'input-fields'}))
    password2 = forms.CharField(label='Repeat Password',
    widget=forms.PasswordInput(attrs={'class':'input-fields'}))


    class Meta:
        model = CustomUser
        fields = ('email', 'country_code','contact_no', 'full_name',)
        widgets = {
            'email':forms.EmailInput(attrs={'class':'input-fields'}),
            'country_code':forms.Select(attrs={'class':'input-fields',
            'style':'width:23%; display:inline;'}),
            'contact_no':forms.TextInput(attrs={'class':'input-fields',
            'style':'width:75%;display:inline;'}),
            'full_name':forms.TextInput(attrs={'class':'input-fields'}),
          
        }
        help_texts = {
            'password': 'Please Create an Strong Password!',
        }
    def __str__(self):
        return self.country_code

    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):  #We Are using here get() becuase we are using password validtion at widgets
            raise forms.ValidationError('Passwords don\'t match.')
        return cd.get('password2')
    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['password2']

    
    
    
    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     self.fields['contact_no'].initial = self.fields['country_code']



class LoginForm(forms.Form):
    username = forms.EmailField( widget=forms.EmailInput(attrs={'class':'input-fields','placeholder':'e.g luke23@email.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-fields','placeholder':'e.g _22@3Ui_su3)32'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""







class UserEditForm(forms.ModelForm):
        class Meta:
            model = CustomUser
            fields = ('email','country_code','contact_no')
            widgets = {
                #'full_name':forms.TextInput(attrs={'class':'form-control w-75'}),
                'email':forms.EmailInput(attrs={'class':'form-control '}),
                'country_code':forms.Select(attrs={'class':'form-select w-25  '}),
                'contact_no':forms.TextInput(attrs={'class':'form-control w-75 '}),
            }
class ProfileEditForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ('full_name','image', )
            widgets = {
                'image':forms.FileInput(attrs={'class':'form-control w-25 '}),
                'full_name':forms.TextInput(attrs={'class':'form-control  '}),
            }