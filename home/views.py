from django.shortcuts import render
from .models import Timetable


def index(request):
    return render(request, 'index.html')

def timetable(request):
    if request.method == "POST":
        branch = request.POST['branch']

         # CHECK THE BRANCH
        if branch == "CSE":
           timetable = Timetable.objects.filter(branch = branch)

        elif branch == "IT":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "CE":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "ETC":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "EEE":
            timetable = Timetable.objects.filter(branch = branch)

        else :
            timetable = Timetable.objects.filter(branch = branch)
           

        context = {'timetable': timetable} 

    else:
        timetable = Timetable.objects.all()
        context = {'timetable':timetable} 
    return render(request, 'timetable.html', context)
