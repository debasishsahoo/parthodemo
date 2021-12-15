from django.shortcuts import render

# Create your views here.
def faculty_profile(request):
    return render(request, 'admin/faculty_profile.html')

def manage_student_faculty(request):
    return render(request, 'admin/manage_student_faculty.html')

def manage_student_cdc(request):
    return render(request, 'admin/manage_student_cdc.html')

def manage_faculty_cdc(request):
    return render(request, 'admin/manage_faculty_cdc.html')

def view_faculty_cdc(request):
    return render(request, 'admin/view_faculty_cdc.html')

def view_student_cdc(request):
    return render(request, 'admin/view_student_cdc.html')

def view_student_faculty(request):
    return render(request, 'admin/view_student_faculty.html')