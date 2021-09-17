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
    timestamp = models.CharField(max_length = 10) # Actually the DateField gave an error just before the submission. Will change the data type during the next task

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
    

    

    
