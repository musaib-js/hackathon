from django.shortcuts import render, redirect
from .models import Timetable, Notification
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from students.models import Student


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

# The Sign Up End Point
def signup(request):
    if request.method == "POST":
        # Get the post parameters
        roll = request.POST['roll']
        name = request.POST['name']
        branch = request.POST['branch']
        year = request.POST['year']
        email = request.POST['email']
        password = request.POST['password']
    
        # Logic to the check the mail ID
        checkid = "@iiit-bh.ac.in"
        if checkid in email:
            # Save the data to the database
            myuser = User.objects.create_user(roll, email, password)
            myuser.first_name = name
            myuser.roll = roll
            myuser.branch = branch
            myuser.year = year
            myuser.email = email
            myuser.save()
            messages.success(request, " Your Account! has been successfully created")
            return redirect('/')
        
        else:
            messages.error(request, "Kindly Signup With The College Mail ID")
            return redirect('/')
            
    else:
        return render(request,  'signup.html')


def handleLogin(request):
    if request.method =='POST':
        roll = request.POST['roll']
        password = request.POST['password']

        user = authenticate(username = roll, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')

        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/')


    return HttpResponse("Login")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')

def profile(request):
    user = request.user
    profile = Student.objects.filter(roll = user).first()
    context = {'profile':profile}
    return render (request, 'profile.html', context)