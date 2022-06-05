from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to ='images/')
    bio = models.TextField(max_length=500,blank=True)
    name = models.CharField(blank=True)
    
    def __str__(self):
        return f'{self.user.username} profile'
    
class Post(models.Model):
    image = models.ImageField(upload_to ='post/')
    name = models.CharField(blank=True)
    likes = models.ManyToManyField(User, related_name='likes',blank=True)
    user = models.ForeignKey(Profile, on_delete=CASCADE,related_name='post')  
    created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return f'{self.user.name} Post'
    
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'
    
    
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'    
    
      
