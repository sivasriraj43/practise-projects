from django.db import models

class College(models.Model):
    
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name

class Program(models.Model):

    program_name = models.CharField(max_length=100)
    college = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self):
        return self.program_name

class Subject(models.Model):

    subject_name= models.CharField(max_length=300)
    program = models.ForeignKey(Program,on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name
