from django.db import models
from django.contrib import admin
class footballplayer (models.Model):
    member_id=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    weight=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()

class footballplayerAdmin(admin.ModelAdmin):
    list_display=('member_id','name','weight','age','email')