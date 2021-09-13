from django.shortcuts import render
from .models import Timetable, Notification


def index(request):
    return render(request, 'index.html')

def timetable(request):
    if request.method == "POST":
        branch = request.POST['branch']
        print(branch) 
         # CHECK THE BRANCH
         
         #22 Batch
        if branch == "CSE-24":
           timetable = Timetable.objects.filter(branch = branch)

        elif branch == "IT-24":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "CE-24":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "ETC-24":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "EEE-24":
            timetable = Timetable.objects.filter(branch = branch)

         # 23 Batch
        elif branch == "CSE-23":
           timetable = Timetable.objects.filter(branch = branch)

        elif branch == "IT-23":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "CE-23":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "ETC-23":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "EEE-23":
            timetable = Timetable.objects.filter(branch = branch)

            #22 Batch

        elif branch == "CSE-22":
           timetable = Timetable.objects.filter(branch = branch)

        elif branch == "IT-22":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "CE-22":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "ETC-22":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "EEE-22":
            timetable = Timetable.objects.filter(branch = branch)

            #21 Batch
        elif branch == "CSE-21":
           timetable = Timetable.objects.filter(branch = branch)

        elif branch == "IT-21":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "CE-21":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "ETC-21":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "EEE-21":
            timetable = Timetable.objects.filter(branch = branch)

        else :
            timetable = Timetable.objects.filter(branch = branch)
           

        context = {'timetable': timetable} 

    else:
        timetable = Timetable.objects.all()
        context = {'timetable':timetable} 
    return render(request, 'timetable.html', context)

def noticeboard(request):
    notice = Notification.objects.all().order_by('-timestamp')
    context = {'notice':notice}
    return render(request, 'noticeboard.html', context)

def notice(request, slug):
    notice = Notification.objects.filter(slug = slug).first()
    context = {'notice':notice}
    return render(request, 'notice.html', context)
