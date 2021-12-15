from django.contrib import admin
from .models import User
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email','first_name','last_name','dept', 'year', 'semester',
                    'enrollment', 'profilepic',
                    'is_cdc', 'is_teacher', 'is_student','status']
    
    

@admin.register(Academic)
class AcademicAdmin(admin.ModelAdmin):
    list_display = ['id', 'Student', 'Treacher', 'studentenrollment', 'studentdept',
                    'studentyear', 'studentsemester', 'subject', 'subjectattendence', 'subjectclass', 'subjectscore', 'subjectmarks', 'date']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'activityname', 'activitydetails', 'activitydate',
                    'activityowner', 'status']

@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ['id','email','massage']