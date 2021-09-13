from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def students(request):
    students =  Student.objects.all()
    context = {'students':students}
    return render(request, 'students.html', context )


def studentdetails(request, name):
    student = Student.objects.filter(name = name).first()
    context = {'student' : student}
    return render(request, "student.html", context)

def search(request):
    query=request.GET['query']
    student= Student.objects.filter(name__icontains=query)
    params={'student': student}
    return render(request, 'search.html', params)