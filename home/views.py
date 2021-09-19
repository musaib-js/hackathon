from django.shortcuts import render, redirect
from .models import Timetable, Notification, todoList, classRep
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from students.models import Student
from students.forms import StudentForm



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

def noticeboard(request):
    user = request.user
    classrep = classRep.objects.filter(roll = user).first()
    if classrep is not None:
        cr = classrep.name
    else:
        cr  = "it's really been tough and tricky"
    notice = Notification.objects.all().order_by('-timestamp')
    context = {'notice':notice, 'cr':cr}
    if request.method == "POST":
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        desc = request.POST['desc']
        author = request.POST['author']
        date = request.POST['date']

        newnotice = Notification(title = title, subtitle = subtitle, desc = desc, author = author, timestamp = date)
        newnotice.save()
        messages.success(request, "Notice Posted Successfully")
        return redirect('/')
         
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

def todo(request):
    user = request.user
    print(user)
    userlogged = Student.objects.filter(roll = user).first()
    branch = userlogged.branch
    year = userlogged.year
    todo = todoList.objects.filter(branch = branch, year = year)
    context = {'todo': todo}
    return render (request, 'todo.html', context)

def update(request):
    user = request.user
    profile = Student.objects.filter(roll = user).first()
    context = {'profile':profile}
    userlogged = Student.objects.filter(roll = user).first()
    form = StudentForm(request.POST, instance = userlogged)  
    if form.is_valid():  
        form.save()  
        messages.success(request, "Details Updated Successfully")
        return redirect('/')  
    return render(request, 'profiel.html', context)  

def polls(request):
    return render(request, 'poll.html')
    
