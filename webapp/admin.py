from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','post']


@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['title','video_url']

@admin.register(TeamMember)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','admission_number','Arka_department','profile_pic']
    
@admin.register(Announcements)
class Noticedmin(admin.ModelAdmin):
    list_display = ['title','body']
    
