from django.db import models
#from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
POST_TYPE = (
    ('ARKA NEWS','ARKA NEWS'),
    ('ARKA FACTS','ARKA FACTS'),
    ('ARKA EVENTS','ARKA EVENTS')
)
DEPARTMENT = (
    ('web-dev','Web Developer'),
    ('graphic','Graphic Designer'),
    ('content','Content-writer'),
    )

class PostModel(models.Model):
     post = models.CharField(max_length=20, choices = POST_TYPE)
     title= models.CharField(max_length=230)
     thumbnail = models.ImageField(upload_to="", null=True, blank=True)
     body= models.TextField()
     image_url = models.CharField(max_length=500, default=None, blank=True)
     uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
        return self.title

STATUS = (
    ('Coordinator','Coordinator'),
    ('Member','Member'),
    ('Founder','Founder'),
    ('Alumnus','Alumnus')
) 

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    status =models.CharField(max_length=100, choices = STATUS)
    Arka_department = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="./members")

    admission_number = models.CharField(max_length=200,blank=True)
    admission_year = models.CharField(max_length=200)
    fb_url =models.URLField(max_length=300, blank=True, null=True)
    linked_url =models.URLField(max_length=300 , blank=True, null=True)
    insta_url =models.URLField(max_length=300 , blank=True, null=True)
    twitter_url =models.URLField(max_length=300 , blank=True, null=True)


class VideoModel(models.Model):
    title=models.CharField( max_length=200)
    video_url =models.URLField( max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
    