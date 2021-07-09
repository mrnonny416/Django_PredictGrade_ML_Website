from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def select(request):
    return render(request, 'select.html')

def forms(request):
    return render(request, 'forms.html')