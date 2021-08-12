from django import forms
class loginForm(forms.Form):
    studentID = forms.CharField(label='Your name', max_length=100)