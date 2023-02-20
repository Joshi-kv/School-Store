from django.db import models

# Create your models here.
class Departments(models.Model):
    department=models.CharField(max_length=250,unique=True)
    links=models.CharField(max_length=500,unique=True)
    
    def __str__(self):
        return '{}'.format(self.department)
    
class Courses(models.Model):
    department=models.ForeignKey(Departments,on_delete=models.CASCADE)
    name=models.CharField(max_length=250,unique=True)
    
    def __str__(self):
        return '{}'.format(self.name)