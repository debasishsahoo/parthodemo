from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .decorator import *
from django.core.exceptions import PermissionDenied
from datetime import datetime
from datetime import date

# Create your views here.


def index(request):
    if request.method == 'POST':
        massageform = MassageForm(request.POST)
        if massageform.is_valid():
            sms = massageform.save(commit=False)
            sms.save()
            messages.success(request, 'Massage Sent Successfully')
            massageform = MassageForm()
            return redirect('index')
        else:
            messages.warning(request, 'Please fill the form correctly')
    else:
        massageform = MassageForm()

    context = {'massageform': massageform}
    return render(request, 'common/index.html',context)










@OnlyAuth
def signup(request):
    if request.method == 'POST':
        SignupForm = SignUpForm(request.POST)
        if SignupForm.is_valid():
            isTeacher=SignupForm.cleaned_data.get('is_teacher')
            isStudent=SignupForm.cleaned_data.get('is_student')
            if isTeacher:
                SignUpUser = SignupForm.save(commit=False)
                SignUpUser.is_teacher = True
                SignUpUser.status = False
                SignUpUser.save()
            elif isStudent:
                SignUpUser = SignupForm.save(commit=False)
                SignUpUser.is_student = True
                SignUpUser.status = True
                SignUpUser.save()
            else:
                messages.warning(request, 'Please Select Your user Type')
                return redirect('signin')
            user = SignupForm.cleaned_data.get('username')
            messages.success(request, 'Account Created for ' + user)
            return redirect('signin')
        else:
            messages.error(request, 'Form is Not Valid')
    else:
        SignupForm = SignUpForm()

    contxt = {'form': SignupForm}
    return render(request, 'common/signup.html', contxt)




@OnlyAuth
def signin(request):
    LM = LoginForm(request.POST or None)
    if request.method == 'POST':
        if LM.is_valid():
            UserName = request.POST.get('username')
            PassWord = request.POST.get('password')
            user = authenticate(request, username=UserName, password=PassWord)
            
            if user is not None and user.is_cdc:
                login(request, user)
                return redirect('manage_student_cdc')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('faculty_profile')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('student_profile')
            else:
                messages.error(request, 'Username or Password is incorrect')
        else:
            messages.error(request, 'Form is Not Valid')
    else:
        LM = LoginForm()
        
    contxt = {'form': LM}
    return render(request, 'common/signin.html', contxt)




@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')


def contact(request):
    return render(request, 'common/contact.html')



@login_required(login_url='signin')
def studentprofile(request):
    if not request.user.is_student:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'admin/notActive.html')
    
    userdata = User.objects.get(pk=request.user.id)
    Activitydata = Activity.objects.filter(activityowner=request.user.id)
    ApproveActivity=[]
    
    for i in Activitydata:
        if i.status == True:
            ApproveActivity.append({
                "activityname":i.activityname,
                "activitydate": i.activitydate,
                "activitydetails":i.activitydetails,
                # "email":i.email,
                # "phoneno":i.phoneno,
                # "yearbatch":i.yearbatch,
                # "last_name": i.last_name,
                # 'dept': i.dept,
                # 'year': i.year,
                # 'semester': i.semester,
                # 'enrollment': i.enrollment,
                # 'profilepic': i.profilepic,
            })
    
    context = {'StudentData': userdata, 'Activitydata': Activitydata, 'ApproveActivity':ApproveActivity,}
    return render(request, 'site/studentprofile.html',context)


@login_required(login_url='signin')
def studentsemester(request):
    if not request.user.is_student:
        raise PermissionDenied
    
    userdata = User.objects.get(pk=request.user.id)
    context = {'StudentData': userdata,}
    return render(request, 'site/studentsemester.html',context)



@login_required(login_url='signin')
def studentattendence(request):
    if not request.user.is_student:
        raise PermissionDenied
    userdata = User.objects.get(pk=request.user.id)
    StudentMarks=Academic.objects.filter(Student=request.user.id)
    context = {'StudentData': userdata,'StudentMarks':StudentMarks}
    return render(request, 'site/studentattendence.html',context)


@login_required(login_url='signin')
def studenteditpro(request):
    if not request.user.is_student:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'admin/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        UserProfileForm = SignUpForm(
            request.POST, request.FILES, instance=userdata)

        if UserProfileForm.is_valid():
            student = UserProfileForm.save(commit=False)
            student.is_student = True
            student.status = True
            UserProfileForm.save()
            messages.success(
                request, 'Profile is Updated. please login again to craete a new Session')
            return redirect('signout')
        else:
            messages.warning(request, UserProfileForm.errors)
    else:
        UserProfileForm = SignUpForm(instance=userdata)
    context = {'StudentData': userdata, 'UserProfileForm': UserProfileForm}
    return render(request, 'site/studenteditpro.html', context)


@login_required(login_url='signin')
def studentaddac(request):
    if not request.user.is_student:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'admin/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    Activitydata = Activity.objects.filter(activityowner=request.user.id)
    if request.method == 'POST':
        ActivityProfileForm = ActivityProfile(request.POST, request.FILES)
        if ActivityProfileForm.is_valid():
            studentActivity = ActivityProfileForm.save(commit=False)
            studentActivity.status = False
            studentActivity.activityowner = request.user.id
            studentActivity.save()
            messages.success(
                request, 'Your Activity Details is submited and wait for CDC process')
            return redirect('student_addac')
        else:
            messages.warning(request, ActivityProfileForm.errors)
    else:
        ActivityProfileForm = ActivityProfile()

    context = {'StudentData': userdata, 'Activitydata': Activitydata,
               'ActivityProfileForm': ActivityProfileForm}
    return render(request, 'site/studentaddac.html', context)












@login_required(login_url='signin')
def facultyprofile(request):
    if not request.user.is_teacher:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'admin/notActive.html')
    userdata = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        UserProfileForm = SignUpForm(
            request.POST, request.FILES, instance=userdata)

        if UserProfileForm.is_valid():
            student = UserProfileForm.save(commit=False)
            student.is_teacher = True
            student.status = True
            UserProfileForm.save()
            messages.success(
                request, 'Profile is Updated. please login again to craete a new Session')
            return redirect('signout')
        else:
            messages.warning(request, UserProfileForm.errors)
    else:
        UserProfileForm = SignUpForm(instance=userdata)
    context = {'StudentData': userdata, 'UserProfileForm': UserProfileForm}
    return render(request, 'admin/faculty_profile.html',context)




@login_required(login_url='signin')
def managestudentfaculty(request):
    if not request.user.is_teacher:
        raise PermissionDenied
    if not request.user.status:
        return render(request,'admin/notActive.html')
    
    userdata = User.objects.get(pk=request.user.id)
    studentdata = User.objects.all()
    allstudent = []

    for i in studentdata:
        if i.is_student == True:
            allstudent.append({
                "id": i.id,
                "first_name": i.first_name,
                "username":i.username,
                "email":i.email,
                "phoneno":i.phoneno,
                "yearbatch":i.yearbatch,
                "last_name": i.last_name,
                'dept': i.dept,
                'year': i.year,
                'semester': i.semester,
                'enrollment': i.enrollment,
                'profilepic': i.profilepic,
            })

    context = {'StudentData': userdata, 'allstudent': allstudent}
    return render(request, 'admin/manage_student_faculty.html', context)

@login_required(login_url='signin')
def managestudentcdc(request):
    if not request.user.is_cdc:
        raise PermissionDenied
    return render(request, 'admin/manage_student_cdc.html')

@login_required(login_url='signin')
def managefacultycdc(request):
    if not request.user.is_cdc:
        raise PermissionDenied
    return render(request, 'admin/manage_faculty_cdc.html')

@login_required(login_url='signin')
def viewfacultycdc(request):
    return render(request, 'admin/view_faculty_cdc.html')

@login_required(login_url='signin')
def viewstudentcdc(request):
    return render(request, 'admin/view_student_cdc.html')

@login_required(login_url='signin')
def viewstudentfaculty(request, pk):
    if not request.user.is_teacher:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'admin/notActive.html')
    userdata = User.objects.get(pk=request.user.id)
    studentdetails = User.objects.get(pk=pk)
    StudentMarks=Academic.objects.filter(Student=pk)
    
    if request.method == 'POST':
        AcademicForm = AcademicProfile(request.POST)
        if AcademicForm.is_valid():
            AcademicUser = AcademicForm.save(commit=False)
            AcademicUser.Student = pk
            AcademicUser.Treacher = request.user.id
            AcademicUser.studentenrollment = studentdetails.enrollment
            AcademicUser.date=date.today()
            AcademicUser.save()
            messages.success(
                request, 'Marks & Attendence is Saved')
            return redirect('manage_student_faculty')
        else:
            messages.warning(request, AcademicForm.errors)
    else:
        AcademicForm = AcademicProfile()
    context = {'StudentData': userdata, 'AcademicForm': AcademicForm,'studentdetails':studentdetails,'StudentMarks':StudentMarks}
    return render(request, 'admin/view_student_faculty.html', context)


