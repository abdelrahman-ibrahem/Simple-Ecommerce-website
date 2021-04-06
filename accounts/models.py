from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# create profile model 

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to='profile')
    entered_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.username)

