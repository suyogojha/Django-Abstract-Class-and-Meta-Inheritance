from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    student_data = Student.objects.all()
    teacher_data = Teacher.objects.all()
    contractor_data = Contractor.objects.all()
    con = {
        'teachers': teacher_data,
        'students': student_data,
        'contractors': contractor_data,
    }
    return render(request, 'home.html', con)