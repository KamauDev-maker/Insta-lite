from django.test import TestCase
from .models import Comment, Profile, Follow,Post
from django.contrib.auth.models import User


class ProfileTestClass(TestCase):
    def setUp(self):
        self.oscar = User(username = "oscar", email = "oscar@gmail.com",password = "4321")
        self.profile = Profile(bio='bio', user= self.oscar)
        self.oscar.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.oscar, User))
        self.assertTrue(isinstance(self.profile, Profile))

class PostTestClass(TestCase):
    def setUp(self) :
        self.profile_test = Profile(name='oscar', user=User(username='kamau'))

        self.image_test = Post(image='default.png', name='test', user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Post))
        
