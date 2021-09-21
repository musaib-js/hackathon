from django.db import models
from django.utils import timezone
from datetime import date


class Notification(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 250)
    subtitle = models.CharField(max_length = 400)
    desc = models.TextField()
    author = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 150)
    timestamp = models.DateField(default = "01-01-2020")

    def __str__(self):
        return self.title +  " by " + self.author

class Timetable(models.Model):
    sno = models.AutoField(primary_key = True)
    subject = models.CharField(max_length = 100)
    teacher = models.CharField(max_length = 100)
    timing = models.CharField(max_length = 20)
    branch = models.CharField(max_length = 10, default = "" )
    days = models.CharField(max_length = 20, default = "")

    def __str__(self):
        return self.subject + " by " +  self.teacher +  " for " + self.branch


class todoList(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 250)
    subject = models.CharField(max_length = 100)
    duedate = models.DateField()
    branch = models.CharField(max_length = 10, default = "")
    year = models.CharField(max_length = 10, default = "")

    def __str__(self):
        return self.title
    
class classRep(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 45)
    roll = models.CharField(max_length = 12)
    branch = models.CharField(max_length = 10)
    year = models.CharField(max_length = 10)

    def __str__(self):
        return self.name + " CR of " + self.branch + self.year

class events(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title
    

    

    
