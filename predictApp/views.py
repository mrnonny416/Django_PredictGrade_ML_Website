from django.shortcuts import redirect, render
from .loginforms import loginForm
from .models import Subject
# Create your views here.
def login(request):
    if request.method == 'POST':
        department = (request.POST.get('studentID'))[2:8]
        if department == '523206':
            request.session['studentID'] = request.POST.get('studentID')
            return redirect('select')
    return render(request, 'login.html', {'form': loginForm})

def select(request):
    studentID = request.session.get('studentID')
    if(studentID == None):
        return redirect('login')
    return render(request, 'select.html')

def forms(request):
    if request.method == 'GET':
        subjectID = request.GET.get('subjectID')
        subject_info = Subject.objects.filter(subjectID=(subjectID))
    return render(request, 'forms.html' ,{'subject_info':subject_info})
