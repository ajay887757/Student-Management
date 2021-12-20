from django.db import models, reset_queries


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    stu_id = models.CharField(max_length=100, unique=True)
    stu_fname = models.CharField(max_length=100, default='')
    stu_lname = models.CharField(max_length=100, default='')
    stu_Day = models.CharField(max_length=10,default='')
    stu_Month = models.CharField(max_length=10, default='')
    stu_Year = models.CharField(max_length=10, default='')
    stu_contact = models.CharField(max_length=10,default='')
    stu_email = models.EmailField(max_length=30,default="")
    stu_room = models.CharField(max_length=6,default='')
    stu_gender = models.CharField(max_length=6,default='')
    Address = models.CharField(max_length=30,default='')
    City = models.CharField(max_length=30,default='')
    Pin_Code = models.CharField(max_length=30,default='')
    State = models.CharField(max_length=30,default='')
    Country = models.CharField(max_length=15,default='')
    COURSES = models.CharField(max_length=15,default='')
    stu_branch = models.CharField(max_length=100, default='')


    def __str__(self):
        return str(self.stu_fname + '\n' + self.stu_lname)
    

class About_me(models.Model):
    About_me_name=models.CharField(max_length=20,null=True)
    About_me_mail=models.CharField(max_length=50,null=True)
    About_me_text=models.CharField(max_length=500,null=True)

    def __str__(self) :
        return self.About_me_name





    