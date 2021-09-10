from django.shortcuts import redirect, render
from .loginforms import loginForm
from .models import Subject ,Subject_refer ,Instructor,menu_subject,department
from .predictors import predict_ENGCE101,predict_ENGCE102,predict_ENGCE103,predict_ENGCE104,predict_ENGCE105,predict_ENGCE106,predict_ENGCE107,predict_ENGCE108,predict_ENGCE109,predict_ENGCE110,predict_ENGCE111,predict_ENGCE112,predict_ENGEL105,predict_ENGEL106

# Create your views here.
def login(request):
    if request.method == 'POST':
        for department_check in department.objects.all():
            departmentID = (request.POST.get('studentID'))[department_check.start_CharField:department_check.end_CharField]
            if departmentID == department_check.department_id :
                request.session['studentID'] = request.POST.get('studentID')
                return redirect('select')
    return render(request, 'login.html', {'form': loginForm})

def select(request):
    studentID = request.session.get('studentID')
    if(studentID == None):
        return redirect('login')
    subject_menu = menu_subject.objects.all()
    subject_info = Subject.objects.all()
    return render(request, 'select.html',{'subject_menu':subject_menu,'subject_info':subject_info})

def forms(request):
    if request.method == 'GET':
        subject_refer_index = []
        subjectID = request.GET.get('subjectID')
        subject_info = Subject.objects.all()
        subject_refer_info = Subject_refer.objects.filter(subjectID=(subjectID))

        for subject_info_roll in subject_info:
            for subject_refer_info_roll in subject_refer_info:
                if(subject_info_roll.subjectID == subject_refer_info_roll.ref_subjectID):
                    subject_refer_index.append(subject_info_roll.subjectID)
                    break
    return render(request, 'forms.html' ,{'subjectID':subjectID ,'subject_info':subject_info ,'subject_refer_info':subject_refer_info ,'subject_refer_index':subject_refer_index})

def reports(request):
    if request.method == 'POST':
        Instructor_number = []
        Predict_result = 50
        GradeRoll = []
        subject_refer_index = []
        subjectID = request.GET.get('subjectID')
        subject_info = Subject.objects.all()
        subject_refer_info = Subject_refer.objects.filter(subjectID=(subjectID))
        for subject_info_roll in subject_info:
            for subject_refer_info_roll in subject_refer_info:
                if(subject_info_roll.subjectID == subject_refer_info_roll.ref_subjectID):
                    subject_refer_index.append(subject_info_roll.subjectID)
                    break
        for subject_refer_index_roll in subject_refer_index:
            grade_roll = request.POST.get('grade_'+subject_refer_index_roll)
            if grade_roll == '4':Grade = 'A'
            elif grade_roll == '3.5':Grade = 'B+'
            elif grade_roll == '3':Grade = 'B'
            elif grade_roll == '2.5':Grade = 'C+'
            elif grade_roll == '2':Grade = 'C'
            elif grade_roll == '1.5':Grade = 'D+'
            elif grade_roll == '1':Grade = 'D'
            elif grade_roll == '0':Grade = 'F'
            else:Grade = 'ยังไม่ได้ลงทะเบียนเรียนหรือถอนรายวิชา'
            GradeRoll.append([subject_refer_index_roll,Grade])

    
#        if subjectID == 'ENGCE101':
#            Predict_result = prediction_ENGCE101(float(request.POST.get('grade_ENGCC304')),float(request.POST.get('grade_FUNMA105')),float(request.POST.get('grade_FUNSC101')),float(request.POST.get('grade_GEBLC103')))
#        elif subjectID == 'ENGCE102':
#            Predict_result = prediction_ENGCE102(float(request.POST.get('grade_ENGCC304')),float(request.POST.get('grade_FUNMA105')),float(request.POST.get('grade_FUNSC101')),float(request.POST.get('grade_GEBLC103')))
#        elif subjectID == 'ENGCE103':
#            Predict_result = prediction_ENGCE103(float(request.POST.get('grade_ENGCC304')),float(request.POST.get('grade_ENGEE106')),float(request.POST.get('grade_FUNSC101')),float(request.POST.get('grade_GEBLC103')))
#        elif subjectID == 'ENGCE104':
#            Predict_result = prediction_ENGCE104(float(request.POST.get('grade_ENGCE102')),float(request.POST.get('grade_ENGCE106')),float(request.POST.get('grade_ENGEE106')),float(request.POST.get('grade_FUNSC101')))
#        elif subjectID == 'ENGCE105':
#            Predict_result = prediction_ENGCE105(float(request.POST.get('grade_ENGCE102')),float(request.POST.get('grade_ENGCE103')),float(request.POST.get('grade_ENGCE106')),float(request.POST.get('grade_ENGEL106')),float(request.POST.get('grade_FUNMA105')),float(request.POST.get('grade_FUNSC101')))
#        elif subjectID == 'ENGCE106':
#            Predict_result = prediction_ENGCE106(float(request.POST.get('grade_ENGCE104')),float(request.POST.get('grade_ENGEL106')),float(request.POST.get('grade_FUNSC101')),float(request.POST.get('grade_GEBLC103')))
#        elif subjectID == 'ENGCE107':
#            Predict_result = prediction_ENGCE107(float(request.POST.get('grade_ENGCE102')),float(request.POST.get('grade_ENGCE104')),float(request.POST.get('grade_ENGCE106')),float(request.POST.get('grade_FUNSC101')))
#        elif subjectID == 'ENGCE108':
#            Predict_result = prediction_ENGCE108(float(request.POST.get('grade_ENGCE105')),float(request.POST.get('grade_ENGCE111')),float(request.POST.get('grade_ENGCE112')))
#        elif subjectID == 'ENGCE109':
#            Predict_result = prediction_ENGCE109(float(request.POST.get('grade_ENGCE104')),float(request.POST.get('grade_ENGCE106')),float(request.POST.get('grade_ENGEL106')))
#        elif subjectID == 'ENGCE110':
#            Predict_result = prediction_ENGCE110(float(request.POST.get('grade_ENGCC304')),float(request.POST.get('grade_ENGEL105')),float(request.POST.get('grade_ENGEL106')))
#        elif subjectID == 'ENGCE111':
#            Predict_result = prediction_ENGCE111(float(request.POST.get('grade_ENGCE103')),float(request.POST.get('grade_ENGCE106')),float(request.POST.get('grade_ENGEL106')),float(request.POST.get('grade_GEBLC103')))
#        elif subjectID == 'ENGCE112':
#            Predict_result = prediction_ENGCE112(float(request.POST.get('grade_ENGCC304')),float(request.POST.get('grade_ENGCE102')),float(request.POST.get('grade_GEBLC103')))
#        elif subjectID == 'ENGEL105':
#            Predict_result = prediction_ENGEL105(float(request.POST.get('grade_ENGCE106')),float(request.POST.get('grade_ENGEL106')),float(request.POST.get('grade_FUNSC101')),float(request.POST.get('grade_GEBLC103')))
#        elif subjectID == 'ENGEL106':
#            Predict_result = prediction_ENGEL106(float(request.POST.get('grade_ENGCE102')),float(request.POST.get('grade_ENGCE106')),float(request.POST.get('grade_ENGEE106')),float(request.POST.get('grade_FUNMA105')),float(request.POST.get('grade_FUNSC101')))#

        
    return render(request, 'reports.html', {'subjectID':subjectID ,'subject_info':subject_info ,'subject_refer_index':subject_refer_index,'Predict_result':Predict_result,'GradeRoll':GradeRoll})


def prediction_ENGCE101(ENGCC304,FUNMA105,FUNSC101,GEBLC103):
    Predict_result = predict_ENGCE101(ENGCC304,FUNMA105,FUNSC101,GEBLC103)
    return Predict_result

def prediction_ENGCE102(ENGCC304,FUNMA105,FUNSC101,GEBLC103):
    Predict_result = predict_ENGCE102(ENGCC304,FUNMA105,FUNSC101,GEBLC103)
    return Predict_result

def prediction_ENGCE103(ENGCC304,ENGEE106,FUNSC101,GEBLC103):
    Predict_result = predict_ENGCE103(ENGCC304,ENGEE106,FUNSC101,GEBLC103)
    return Predict_result

def prediction_ENGCE104(ENGCE102,ENGCE106,ENGEE106,FUNSC101):
    Predict_result = predict_ENGCE104(ENGCE102,ENGCE106,ENGEE106,FUNSC101)
    return Predict_result

def prediction_ENGCE105(ENGCE102,ENGCE103,ENGCE106,ENGEL106,FUNMA105,FUNSC101):
    Predict_result = predict_ENGCE105(ENGCE102,ENGCE103,ENGCE106,ENGEL106,FUNMA105,FUNSC101)
    return Predict_result

def prediction_ENGCE106(ENGCE104,ENGEL106,FUNSC101,GEBLC103):
    Predict_result = predict_ENGCE106(ENGCE104,ENGEL106,FUNSC101,GEBLC103)
    return Predict_result

def prediction_ENGCE107(ENGCE102,ENGCE104,ENGCE106,FUNSC101):
    Predict_result = predict_ENGCE107(ENGCE102,ENGCE104,ENGCE106,FUNSC101)
    return Predict_result

def prediction_ENGCE108(ENGCE105,ENGCE111,ENGCE112):
    Predict_result = predict_ENGCE108(ENGCE105,ENGCE111,ENGCE112)
    return Predict_result

def prediction_ENGCE109(ENGCE104,ENGCE106,ENGEL106):
    Predict_result = predict_ENGCE109(ENGCE104,ENGCE106,ENGEL106)
    return Predict_result

def prediction_ENGCE110(ENGCC304,ENGEL105,ENGEL106):
    Predict_result = predict_ENGCE110(ENGCC304,ENGEL105,ENGEL106)
    return Predict_result

def prediction_ENGCE111(ENGCE103,ENGCE106,ENGEL106,GEBLC103):
    Predict_result = predict_ENGCE111(ENGCE103,ENGCE106,ENGEL106,GEBLC103)
    return Predict_result

def prediction_ENGCE112(ENGCC304,ENGCE102,GEBLC103):
    Predict_result = predict_ENGCE112(ENGCC304,ENGCE102,GEBLC103)
    return Predict_result

def prediction_ENGEL105(ENGCE106,ENGEL106,FUNSC101,GEBLC103):
    Predict_result = predict_ENGEL105(ENGCE106,ENGEL106,FUNSC101,GEBLC103)
    return Predict_result

def prediction_ENGEL106(ENGCE102,ENGCE106,ENGEE106,FUNMA105,FUNSC101):
    Predict_result = predict_ENGEL106(ENGCE102,ENGCE106,ENGEE106,FUNMA105,FUNSC101)
    return Predict_result
