from django.db import models
from django.db.models.fields import AutoField
# Create your models here.
class Subject_refer(models.Model):
    order = models.AutoField(primary_key=True)
    subjectID = models.CharField(max_length=20)
    ref_subjectID = models.CharField(max_length=20)
    subject_instructor_ID = models.CharField(max_length=150)
    
    def __str__(self):
        return self.subjectID
class Subject(models.Model):
    order = models.AutoField(primary_key=True)
    subjectID = models.CharField(max_length=20)
    subject_name_th = models.CharField(max_length=200)
    subject_name_eng = models.CharField(max_length=200)
   
    def __str__(self):
        return self.subjectID
class Instructor(models.Model):
    order = models.AutoField(primary_key=True)
    Instructor_ID = models.CharField(max_length=20)
    Instructor_name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.Instructor_ID

class menu_subject(models.Model):
    order = models.AutoField(primary_key=True)
    menu_id = models.IntegerField()
    subjectID = models.CharField(max_length=20)
    img_menu = models.CharField(max_length=124)
    
    def __str__(self):
        return self.subjectID

class department(models.Model):
    order = models.AutoField(primary_key=True)
    department_id = models.CharField(max_length=20)
    department_name = models.CharField(max_length=124)
    start_CharField = models.IntegerField()
    end_CharField = models.IntegerField()
    
    def __str__(self):
        return self.department_name