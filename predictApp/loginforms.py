from django import forms
class loginForm(forms.Form):
    studentID = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'myfieldclass','placeholder':'กรุณากรอกรหัสนักศึกษา'}))