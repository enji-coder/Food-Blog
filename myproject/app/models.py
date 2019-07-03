from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=30)
    otp=models.IntegerField(default=8457)
    profile_pic=models.FileField(upload_to='img/',blank=True,default='img/avatar.png')
    
class GalleryView(models.Model):
    pic=models.FileField(upload_to='img/',blank=True,default='img/avatar.png')

class VideoGallery(models.Model):
    name=models.CharField(max_length=50)
    videofile=models.FileField(upload_to='videos/',null=True,verbose_name="video file")

class AudioGallery(models.Model):
    name=models.CharField(max_length=50)
    audiofile=models.FileField(upload_to='audio/')

class Comments(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=80)
    message=models.CharField(max_length=500)