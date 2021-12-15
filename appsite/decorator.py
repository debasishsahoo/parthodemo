from django.http import HttpResponse
from django.shortcuts import redirect


def OnlyAuth(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_cdc:
                return redirect('manage_student_cdc')
            elif request.user.is_teacher:
                return redirect('faculty_profile')
            elif request.user.is_student:
                return redirect('student_profile')
            else:
                return view_func(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func