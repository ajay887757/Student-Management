from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    stu_id = models.CharField(max_length=100, unique=True)
    stu_fname = models.CharField(max_length=100, default='')
    stu_lname = models.CharField(max_length=100, default='')
    stu_branch = models.CharField(max_length=100, default='')
    stu_age = models.IntegerField(default='15')
    stu_contact = models.IntegerField(default='')

    def __str__(self):
        return str(self.stu_fname + '\n' + self.stu_lname)