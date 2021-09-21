# Geeks Fiesta Hackathon
The project is aimed at developing and implementing a website having a notice board, timetable and a login system for the students.
We are using the technologies HTML, CSS and JS for the frontend, which is handled by both Lopamudra Mallick and Musaib Altaf
For the backend, we're using Python's Django framework, which is handled by Musaib Altaf

# Timetable part
This part shows the class timetable of every branch. The data is rendered from the database and has a proper backend instead of harcoding the tables as the timetables can change at any time. A student is supposed to select his/her branch from the select menu and then press the view button, which displays the time table of the selected branch.

# Notice Board Part
This part shows the notice updates by the college. This data too is rendered from the database and has a proper backend instead of harcoding the notifications. The tables displays the notice date, author and the notice title. The 'Read More' link navigates the user to the page where the complete notice details are shown.


# Students Part
This part displays the list of the students who have been added to the database. Just like the MUMS system displays the list of the students, which is added by the college authorities at the backend side. Upon clicking the ID of the student, the complete details of the student are shown in a proper manner including all his details with his image. A search functionality has been added where anyone can type the name of the student and he can find that among the long and lengthy list.


# Sign Up and Login Part
Sign up part creates the account of the user. The student is supposed to give his name, ID, branch, year, email and set a password for his account. The user is supposed to login with these credentials then. When a user signs up with his details, he can see his profile according to the credentials provided by him. Here the criteria set in the backend is that the ID of the logged in student is matched with the student details at the backend and the data is rendered.


# Profile Part
Every user upon signing in can check his profile. He/She is allowed to update his/her details. When the user logs into the site, he can view his profile, where there's an 'Edit Profile' button, which upon clicking displays a modal containing a form, where a user can submt the details that are to be updated and they'd get updated in the real time.

# CR Previliges
Only the CR's can post, edit and delete a notice from the notice board. The two CRs are Shourya Garg and Lopamudra MAllick whose credentials are given below.
 Username: B120059
 Pass: abcd1234

 Username = B120030
 Pass: lopa1234

# Bonus Tasks
The bonus task that we have implemented as of now is that a student can only signup with his college mail ID, which would be provided to the enrolled students only. So, this would restrict the outsiders to signup and then login to the site.

Secondly, we have added a todolist for each branch. The logic used is that when a user is logged into the site, he'd be shown a 'To-do List' button and upon clicking the button, the todolist of his particular branch and year are shown. The button is not shown to the visitors who are not logged in.

