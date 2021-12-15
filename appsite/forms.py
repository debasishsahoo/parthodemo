from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django.forms.models import ModelForm
from .models import User
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'
    
    
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Your Username *"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder":"Password *"
            }
        )
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "First Name *"
        }))
    
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Last Name *"
        }))
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Username *"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id":"newPw",
                "placeholder":"Password *"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id":"newCPw",
                "onkeyup":"fun()",
                "placeholder":"Confirm Password *",
                
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Your Email *"
            }
        )
    )

    is_cdc = forms.BooleanField(
        required = False,
        widget=forms.CheckboxInput(
            attrs={
                "class": " cbl"
            }
        )
    )
    is_teacher = forms.BooleanField(
        required = False,
        widget=forms.CheckboxInput(
            attrs={
                "class": " cbl",
                "id":"check2"
            }
        )
    )
    is_student = forms.BooleanField(
        required = False,
        widget=forms.CheckboxInput(
            attrs={
                "class": " cbl",
                "id":"check1",
                "checked":"true"
            }
        )
    )
    dept = forms.CharField(
        widget=forms.Select(
            choices=DeptChoice,
            attrs={
                'class': 'form-control',
                
            }))
    year = forms.CharField(
        widget=forms.Select(
            choices=YearChoice,
            attrs={
                'class': 'form-control'
            }))
    yearbatch = forms.CharField(
        required=False,
        widget=forms.Select(
            choices=Yearbatch,
            attrs={
                'class': 'form-control'
            }))
    semester = forms.CharField(
        widget=forms.Select(
            choices=SemChoice,
            attrs={
                'class': 'form-control'
            }))
    enrollment = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enrollment Number *"
            }))
    regno = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Registration Number *"
            }))
    jyear = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Joining Year *"
            }))
    
    phoneno = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Phone No *"
            }))
    
    
    education= forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':'2',
                'placeholder': "Education Details *"
            }))
    
    address= forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':'2',
                'placeholder': "Home Address *"
            }))

    skill= forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':'2',
                'placeholder': "Skill *"
            }))
    
    project= forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':'2',
                'placeholder': "Project *"
            }))
    
    profilepic = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                # 'class': 'custom-file-input',
                'id': "customFile",
                'onchange': "readURL(this);",
                'style': "display: none;"
            }
        ))


    class Meta:
        model = User
        fields = ('first_name','last_name','username','phoneno','yearbatch','jyear','regno','education','address','skill','project','email', 'password1', 
                  'password2', 'is_cdc', 'is_teacher', 'is_student','dept','year','semester',
                  'enrollment', 'profilepic',)
        
        
class ActivityProfile(forms.ModelForm):
    activityname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Activity Name...."
            }))

    activitydate = forms.DateField(
        widget=DateInput(attrs={
            'class': 'form-control'
        }))

    activitydetails = forms.Textarea()

    class Meta:
        model = Activity
        fields = ('activityname', 'activitydetails', 'activitydate',
                  'activityowner', 'status')



class AcademicProfile(forms.ModelForm):
    studentdept = forms.CharField(
        widget=forms.Select(
            choices=DeptChoice,
            attrs={
                'class': 'form-control'
            }))
    studentyear = forms.CharField(
        widget=forms.Select(
            choices=YearChoice,
            attrs={
                'class': 'form-control'
            }))
    studentsemester = forms.CharField(
        widget=forms.Select(
            choices=SemChoice,
            attrs={
                'class': 'form-control'
            }))

    subject = forms.CharField(
        widget=forms.Select(
            choices=SubjectChoice,
            attrs={
                'class': 'form-control'
            }))

    subjectattendence = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Total Attendes of Student.."
            }))
    subjectclass = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Total No of Classes.."
            }))
    subjectscore = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Score of Student..."
            }))
    subjectmarks = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Total Marks..."
            }))
    studentenrollment = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enrollment Number.."
            }))

    class Meta:
        model = Academic
        fields = ('Student', 'Treacher', 'studentenrollment', 'studentdept',
                  'studentyear', 'studentsemester', 'subject', 'subjectattendence', 'subjectclass', 'subjectscore', 'subjectmarks', 'date')


class MassageForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={

                "placeholder":"Your Email *",
                'background': 'transparent',
                'border': 'none',
                'outline': 'none',
                'color': 'white',
                'width': '100%',
                'border-bottom': '2px solid #1a1a1a',
            }
        )
    )
    
    massage= forms.CharField(
        widget=forms.Textarea(
            attrs={
                'margin-top': '5px',
                'background': 'transparent',
                'border': 'none',
                'outline': 'none',
                'color': 'white',
                'width': '100%',
                'rows':'2',
                "cols":'25',
                'border-bottom': '2px solid #1a1a1a',
                'placeholder': "Massage *",

            }))
    
    class Meta:
        model = Massage
        fields = ('email','massage')


