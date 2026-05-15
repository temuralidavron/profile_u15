from django.db import models

from accounts.models import CustomUser


# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='blog/',blank=True,null=True)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='blogs')
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

