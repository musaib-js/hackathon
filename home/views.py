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
