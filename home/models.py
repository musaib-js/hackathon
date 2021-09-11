from django.db import models


class Notification(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 250)
    subtitle = models.CharField(max_length = 400)
    desc = models.TextField()
    author = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 150)

    def __str__(self):
        return self.title +  " by " + self.author

class Timetable(models.Model):
    sno = models.AutoField(primary_key = True)
    subject = models.CharField(max_length = 100)
    teacher = models.CharField(max_length = 100)
    timing = models.CharField(max_length = 20)
    branch = models.CharField(max_length = 10, default = "" )

    def __str__(self):
        return self.subject + " by " +  self.teacher +  " for " + self.branch
    

    
