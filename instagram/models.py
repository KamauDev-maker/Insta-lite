from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to ='images/',default= 'static/images/default-img.jpg')
    bio = models.TextField(max_length=500,blank=True)
    name = models.CharField(max_length = 200,blank=True)

    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user
        
    def save_user(self):
        self.save()   

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    
    def __str__(self):
        return f'{self.user.username} profile'
    
class Post(models.Model):
    image = models.ImageField(upload_to ='post/')
    name = models.CharField(max_length=200,blank=True)
    likes = models.ManyToManyField(User, related_name='user',blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='post')  
    created = models.DateTimeField(auto_now_add=True,null=True)
    
    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return f"/post/{self.id}"

    @property
    def get_all_comments(self):
        return self.comments.all()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f'{self.user.name} Post'
    
class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.post, self.name)
    
    
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'    
    
      
