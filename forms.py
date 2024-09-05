from django import forms
class student(forms.Form):
    NAME = forms.CharField(label='Your Name')
    FATHERS_NAME = forms.CharField()
    MOTHERS_NAME = forms.CharField()
    DOB = forms.DateField()
    EMAIL = forms.EmailField()
    CONTACT = forms.IntegerField()
   
    ADDRESS = forms.CharField()
    PINCOAD = forms.IntegerField()