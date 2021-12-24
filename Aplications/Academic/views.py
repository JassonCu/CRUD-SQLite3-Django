from django.shortcuts import redirect, render
from .models import Course
from django.contrib import messages

# Create your views here.
def home(request):
    courses = Course.objects.all()
    messages.success(request, 'Listed Courses!')
    return render(request, "courseManagement.html", {"Courses" : courses})

def registerCourse(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']
    credit = request.POST['numCredit']
    
    course = Course.objects.create(code=code, name=name, credit=credit)
    messages.success(request, 'Registered Courses!')
    return redirect('/')

def editCourse(request, code):
    course = Course.objects.get(code=code)
    return render(request, "editCourse.html", {"course": course})

def editTheCourse(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']
    credit = request.POST['numCredit']

    course = Course.objects.get(code=code)
    course.name = name
    course.credit = credit
    course.save()

    messages.success(request, 'Edited Course!')

    return redirect('/')

def deleteCourse(request, code):
    course = Course.objects.get(code=code)
    course.delete()

    messages.success(request, 'Deleted Course!')

    return redirect('/')