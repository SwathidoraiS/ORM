# Ex02 Django ORM Web Application
## Date: 18.10.2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import footballplayer,footballplayerAdmin
admin.site.register(footballplayer,footballplayerAdmin)
```

## OUTPUT
![Alt text](<Screenshot (1).png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
