from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.






DeptChoice = [
    ('', 'Depertment'),
    ('Not Applicable', 'Not Applicable'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Civil Engineering', 'Civil Engineering'),
    ('Electrical Engineering', 'Electrical Engineering'),
    ('ComputerScience Engineering', 'Computer Science Engineering'),
    ('Electronics & Communication Engineering', 'Electronics & Communication Engineering'),
]
YearChoice = [
    ('', 'Year'),
    ('Not Applicable', 'Not Applicable'),
    ('First Year', 'First Year'),
    ('Second Year', 'Second Year '),
    ('Third Year', 'Third Year'),
    ('Fourth Year', 'Fourth Year'),
]
Yearbatch = [
    ('', 'Batch'),
    ('2014-18', '2014-18'),
    ('2015-19', '2015-19'),
    ('2016-20', '2016-20'),
    ('2017-21', '2017-21'),
    ('2018-22', '2018-22'),
    ('2019-23', '2019-23'),
    
]
SemChoice = [
    ('', 'Semester'),
    ('Not Applicable', 'Not Applicable'),
    ('1st Semester', 'First Semester'),
    ('2nd Semester', 'Second Semester '),
    ('3rd Semester', 'Third Semester'),
    ('4th Semester', 'Fourth Semester'),
    ('5th Semester', 'Fifth Semester'),
    ('6th Semester', 'Sixth Semester'),
    ('7th Semester', 'Seventh Semester'),
    ('8th Semester', 'Eightth Semester'),
]

SubjectChoice = [
    # Five Paper from each Streem
    ("Mathematics", "Mathematics"),
    ("Data Structure & Algorithms", "Data Structure & Algorithms"),
    ("Circuit Theory & Networks", "Circuit Theory & Networks"),
    ("Computer Organisation", "Computer Organisation"),
    ("Digital Electronics & Logic Design", "Digital Electronics & Logic Design"),
    ("Principles of Programming Language", "Principles of Programming Language"),
    ("Formal Language & Automata Theory", "Formal Language & Automata Theory"),
    ("Operation Research & Optimization Techniques",
     "Operation Research & Optimization Techniques"),
    ("Principles of Communication Engg", "Principles of Communication Engg"),
    ("Advanced Computer Architecture", "Advanced Computer Architecture"),
    ("Operating System", "Operating System"),
    ("Database Management System", "Database Management System"),
    ("Design & Analysis of Algorithm", "Design & Analysis of Algorithm"),
    ("Microprocessor & Microcontrollers", "Microprocessor & Microcontrollers"),
    ("Control System", "Control System"),
    ("Computer network", "Computer network"),
    ("Software Engineering", "Software Engineering"),
    ("Computer Graphics & Multimedia", "Computer Graphics & Multimedia"),
    ("System Software and Administration", "System Software and Administration"),
    ("Object Technology & UML", "Object Technology & UML"),
    ("Language  Processor", "Language  Processor",),
    ("Artificial Intelligence", "Artificial Intelligence"),
    ("Visual Programming and Web technology",
     "Visual Programming and Web technology"),
    ("Financial Management and accounts", "Financial Management and accounts"),
]



class User(AbstractUser):
    dept = models.CharField(
        max_length=40, choices=DeptChoice, default='Computer Science')
    year = models.CharField(
        max_length=40, choices=YearChoice, default='First Year')
    yearbatch = models.CharField(
        max_length=40, choices=Yearbatch, default='2019-23')
    semester = models.CharField(
        max_length=40, choices=SemChoice, default='First Semester')
    enrollment = models.CharField(max_length=70, null=True, blank=True)
    regno = models.CharField(max_length=70, null=True, blank=True)
    jyear = models.CharField(max_length=4, null=True, blank=True)
    phoneno = models.CharField(max_length=70, null=True, blank=True)
    education = models.CharField(max_length=150,null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    skill = models.CharField(max_length=150,null=True, blank=True)
    project = models.CharField(max_length=100,null=True, blank=True)
    profilepic = models.ImageField(
        upload_to='profile_pic/', null=True, blank=True, default='https://res.cloudinary.com/mern-commerce/image/upload/v1633459954/usericon_hpewnq.png')
    is_cdc= models.BooleanField('Is cdc', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_student = models.BooleanField('Is student', default=False)
    status=models.BooleanField(default=True)

class Academic(models.Model):
    # Need For Student Tracker Only
    Student = models.PositiveIntegerField(null=True, blank=True)
    Treacher = models.PositiveIntegerField(null=True, blank=True)
    studentenrollment = models.CharField(max_length=100)
    studentdept = models.CharField(
        max_length=40, choices=DeptChoice, default='Computer Science')
    studentyear = models.CharField(
        max_length=40, choices=YearChoice, default='First Year')
    studentsemester = models.CharField(
        max_length=40, choices=SemChoice, default='First Semester')
    subject = models.CharField(
        max_length=80, choices=SubjectChoice, default='Mathematics')
    subjectattendence = models.CharField(max_length=100, null=True, blank=True)
    subjectclass = models.CharField(max_length=100, null=True, blank=True)
    subjectscore = models.CharField(max_length=100, null=True, blank=True)
    subjectmarks = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)


class Activity(models.Model):
    # Need For Student Tracker Only
    activityname = models.CharField(max_length=70)
    activitydetails = RichTextField(null=True, blank=True)
    activitydate = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    activityowner = models.PositiveIntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
    
    
class Massage(models.Model):
    email=models.EmailField(blank=True)
    massage=models.TextField(max_length=200,blank=True)