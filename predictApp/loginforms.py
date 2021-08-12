from django import forms
class loginForm(forms.Form):
    studentID = forms.CharField(label='รหัสนักศึกษา', max_length=100)