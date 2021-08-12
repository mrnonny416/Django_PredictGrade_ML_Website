from django.shortcuts import render
from .loginforms import loginForm
# Create your views here.
def login(request):
    showID = ''
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'login.html', {'form': loginForm})

def select(request):
    return render(request, 'select.html')

def forms(request):
    return render(request, 'forms.html')