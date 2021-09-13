from django.db import models

class Student(models.Model):
    roll = models.CharField(max_length = 20, primary_key = True)
    name = models.CharField(max_length = 150)
    branch = models.CharField(max_length = 10)
    year = models.CharField(max_length = 5)
    residence = models.CharField(max_length = 250)
    profile = models.ImageField(upload_to = 'media')
    achievements  = models.TextField()
    skills = models.CharField(max_length = 150, default = "")
    email = models.EmailField(max_length = 150, default = "")
    phone = models.IntegerField(default = "00000000000")
    interests = models.CharField(max_length = 200, default = "")
    society = models.CharField(max_length = 600, default = "")


    def __str__(self):
        return self.name + " of " + self.branch

