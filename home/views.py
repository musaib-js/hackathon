from django.shortcuts import render, redirect
from .models import Timetable, Notification, todoList, classRep, events
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from students.models import Student
from students.forms import StudentForm
from .forms import notificationForm



def index(request):
    notice = Notification.objects.all().order_by('-timestamp')[0:5].filter()
    event = events.objects.all()[0:5].filter()
    context = {'notice':notice, 'event':event}
    return render(request, 'index.html', context)

def timetable(request):
    if request.method == "POST":
        branch = request.POST['branch']

         # CHECK THE BRANCH
        if branch == "CSE-21":
           timetable = Timetable.objects.filter(branch = branch)

        elif branch == "CSE-22":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "CSE-23":
            timetable = Timetable.objects.filter(branch = branch)

        elif branch == "CSE-24":
            timetable = Timetable.objects.filter(branch = branch)

        else :
            timetable = Timetable.objects.filter(branch = "CSE-24")
           

        context = {'timetable': timetable} 

    else:
        timetable = Timetable.objects.all()
        context = {'timetable':timetable} 
    return render(request, 'timetable.html', context)

def noticeboard(request):
    #Check the logged in user
    user = request.user
    #Check if the logged in user is a CR or not
    classrep = classRep.objects.filter(roll = user).first()
    # If he is a CR, get his name
    if classrep is not None:
        cr = classrep.name
    #If not then pass a string so that the query does not return a null value    
    else:
        cr  = "it's really been tough and tricky"
    # Now get the notices from the notice board    
    notice = Notification.objects.all().order_by('-timestamp')
    #Pass the notice object and cr (Name of CR) to the context
    context = {'notice':notice, 'cr':cr}
    #Create a Random String
    from django.utils.crypto import get_random_string 
    unique_id = get_random_string(length=32)
    #Check for the post request
    if request.method == "POST":
        #If it is a post request, then get the parameters
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        desc = request.POST['desc']
        author = request.POST['author']
        date = request.POST['date']
        slug = unique_id
           
        #Create an object and save that in the Notification model
        newnotice = Notification(title = title, subtitle = subtitle, desc = desc, author = author, timestamp = date, slug = slug)
        newnotice.save()
        messages.success(request, "Notice Posted Successfully")
        return redirect('/')
         
    return render(request, 'noticeboard.html', context)

def notice(request, slug):
    #Check the logged in user
    user = request.user
    #Check if the logged in user is a CR or not
    classrep = classRep.objects.filter(roll = user).first()
    # If he is a CR, get his name
    if classrep is not None:
        cr = classrep.name
    #If not then pass a string so that the query does not return a null value    
    else:
        cr  = "it's really been tough and tricky"
    notice = Notification.objects.filter(slug = slug).first()
    context = {'notice':notice, 'cr':cr}
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
    else:
         messages.error(request, "Fill the form correctly")
    return render(request, 'profile.html', context)  

def polls(request):
    return render(request, 'poll.html')

def noticeupdate(request, slug):
    notice = Notification.objects.filter(slug = slug).first()
    form = notificationForm(request.POST, instance = notice)  
    print(form)
    if form.is_valid():  
        form.save()  
        messages.success(request, "Notice Updated Successfully")
        return redirect('/')
    else:
         messages.error(request, "Fill the form correctly")

    return render(request, 'index.html') 

def delete(request, slug):
    notice = Notification.objects.filter(slug = slug).first()
    notice.delete()
    messages.success(request, "Notice Deleted Successfully")
    return redirect ('/')