
from home.models import Contact
from django import forms

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact', 'query',)

        widgets = {
            'name':forms.TextInput( attrs={'type':'text' ,
                'class':'form-control '}),
            'email':forms.EmailInput(
                attrs={'type':'email' ,
                'class':'form-control  '}),
            'contact':forms.TextInput( attrs={'type':'tel' ,
                'class':'form-control  '}),
            'query':forms.Textarea( attrs={'type':'text' ,
                'class':'form-control ','aria-label':'With textarea'}),
          
        }