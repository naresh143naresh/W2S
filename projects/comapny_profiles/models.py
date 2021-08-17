from django.db import models

class Postion(models.Model):
    manager = models.CharField(max_length=100)
    employee = models.CharField(max_length=100)
    def __str__(self):
        return self.manager, self.employee

class company(models.Model):
    postions = models.ForeignKey(Postion, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    skills = models.TextField()
    emp_percentage = models.TextField()
    def __str__(self):
        return self.postions, self.employee_name, self.skills,self.emp_percentage,











