# User Model Logic
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import randint




class User(AbstractUser):
    """
    Custom user model.
    """
    USER_TYPES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("admin", "Admin"),
    ]
    name=models.CharField(max_length=200)
    user_id=models.CharField(max_length=100,editable=False,primary_key=True)
    user_type = models.CharField(max_length=100, choices=USER_TYPES) 
    user_image = models.FileField(upload_to="path-to-upload",null=True,blank=True)
    #college = models.ForeignKey('api.College', on_delete=models.PROTECT, null=True)

    date_of_birth=models.DateField(verbose_name='Date of birth',null=True,blank=True)
    email=models.EmailField()
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_password = self.password
        
    @property
    def id(self):
        return self.pk
        
        
    
    def save(self, *args, **kwargs):
        """
        Override save method to hash password only if it's set or changed.
        """
        if self.password and (not self.pk or self._state.adding or self.password != self._original_password):
            self.set_password(self.password)
        if not self.user_id and self._state.adding:
            self.user_id=f"{self.name}-{self.user_type}-{randint(10000,99999)}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        if self.is_superuser:
            return self.name
        return self.user_id

class Student(models.Model):
    """
    Model representing a student.
    """
    GENDER_CHOICE=[
        ('Male','Male'),
        ('Female','Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=300)

    first_name=models.CharField(max_length=100,blank=True,null=True,verbose_name='First Name')
    last_name=models.CharField(max_length=100,blank=True,null=True,verbose_name='Last Name')
    email=models.EmailField(blank=True,default=True,verbose_name='E-mail')
    phone=models.IntegerField(max_length=10,verbose_name='Phone')
    Dateofbirth=models.DateField(blank=True,null=True)
    Gender=models.CharField(choices=GENDER_CHOICE,max_length=23,blank=True,null=True)
    Address=models.TextField(null=True,blank=True)
    State=models.CharField(max_length=100,default='Tamil Nadu',null=True,blank=True)
    Country=models.CharField(max_length=120,default='India',null=True,blank=True)
    


    student_id=models.CharField(max_length=100,editable=False,primary_key=True)
    #program=models.ForeignKey('api.Program',on_delete=models.PROTECT,null=True,blank=True) 
    
    def save(self, *args, **kwargs):
        """
        Override save method to set the student's name based on the user's username.
        """
      
        self.name = self.user.username
        self.student_id=self.user.user_id
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.name}-{self.student_id}"

class Teacher(models.Model):
    """
    Model representing a teacher.
    """
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=300)
    teacher_id=models.CharField(max_length=100,editable=False,primary_key=True)
        
    def save(self, *args, **kwargs):
        """
        Override save method to set the teacher's name based on the user's username.
        """
        self.name = self.user.username
        self.teacher_id=self.user.user_id
        
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.name}-{self.teacher_id}"

# class profiledetails(models.Model):
#     name=models.CharField(max_length=100)
    

@receiver(post_save, sender=User)
def custom_user_created(sender, instance, created, **kwargs):
    """
    Signal handler for custom user creation.
    """
    if created:
        if instance.user_type == 'student':
            student = Student.objects.create(user=instance)
            student.save()
        elif instance.user_type == 'teacher':
            teacher = Teacher.objects.create(user=instance)
            teacher.save()


























































































