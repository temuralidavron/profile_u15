from django.contrib.auth.models import AbstractUser
from django.db import models

class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    VIEWER = 'viewer', 'Viewer'
    MANAGER = 'manager', 'Manager'



class CustomUser(AbstractUser):
    phone=models.CharField(max_length=13,unique=True)
    role=models.CharField(max_length=20,choices=UserRole,default=UserRole.VIEWER)

    def __str__(self):
        return self.username




class Profile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='profile')
    avatar=models.ImageField(upload_to='profile/',blank=True,null=True,default='nur/personcha.png')
    age=models.PositiveIntegerField(blank=True,null=True)
    bio=models.TextField(blank=True,null=True)


    def __str__(self):
        return f"{self.user.username} ning yoshi {self.age}da"
