"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from appsite import views
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "CDC ADMIN"
admin.site.site_title = "CDC ADMIN"
admin.site.index_title = "CDC ADMIN"

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('appsite.urls')),
    # path('', include('appadmin.urls')),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('contact/', views.contact, name='contact'),
    path('student_profile/', views.studentprofile, name='student_profile'),
    path('student_semester/', views.studentsemester, name='student_semester'),
    path('student_attendence/', views.studentattendence, name='student_attendence'),
    path('student_editpro/', views.studenteditpro, name='student_editpro'),
    path('student_addac/', views.studentaddac, name='student_addac'),
    path('faculty_profile/', views.facultyprofile, name='faculty_profile'),
    path('manage_student_faculty/', views.managestudentfaculty, name='manage_student_faculty'),
    path('manage_student_cdc/', views.managestudentcdc, name='manage_student_cdc'),
    path('manage_faculty_cdc/', views.managefacultycdc, name='manage_faculty_cdc'),
    path('view_faculty_cdc/', views.viewfacultycdc, name='view_faculty_cdc'),
    path('view_student_cdc/', views.viewstudentcdc, name='view_student_cdc'),
    path('view_student_faculty/<int:pk>', views.viewstudentfaculty, name='view_student_faculty'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)