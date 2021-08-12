from django.shortcuts import redirect, render
from .loginforms import loginForm
# Create your views here.
def login(request):
    if request.method == 'POST':
        print(request.POST)
        department = (request.POST.get('studentID'))[2:8]
        if department == '523206':
            return redirect('select')
    return render(request, 'login.html', {'form': loginForm})

def select(request):
    return render(request, 'select.html')

def forms(request):
    return render(request, 'forms.html')
