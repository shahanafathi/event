# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.
# # class CustomeUser(AbstractUser):
# #      = models.IntegerField(null=True, blank=True)
# #     address=models.CharField(null=True, blank=True,max_length=1000)
# #     phone_number = models.IntegerField(null=True, blank=True, unique=False) 

# class CustomeUser(AbstractUser):
#     phone_number = models.IntegerField(null=True, blank=True, unique=True) 
#     usertype=models.CharField(max_length=200)
#     address=models.CharField(null=True,blank=True,max_length=100)
#     place=models.CharField(null=True,blank=True,max_length=500)
#     status=models.CharField(max_length=100,null=True, blank=True,default='pending')
#     Image=models.FileField(null=True,blank=True)
#     email = models.EmailField(unique=True)
#     # def __str__(self):
#     #     return self.name

# class event_register(models.Model):
#     phone_number = models.IntegerField(null=True, blank=True, unique=True) 
#     title=models.CharField(null=True,blank=True,max_length=100)
#     description = models.CharField(null=True, blank=True, max_length=100)
#     date = models.DateField()
#     address=models.CharField(null=True,blank=True,max_length=100)

#     location=models.CharField(null=True,blank=True,max_length=100)
#     def __str__(self):
#         return self.title

# class event_list(models.Model):
#     phone_number = models.IntegerField(null=True, blank=True, unique=True) 
#     title=models.CharField(null=True,blank=True,max_length=100)
#     description = models.CharField(null=True, blank=True, max_length=100)
#     date = models.DateField()
#     address=models.CharField(null=True,blank=True,max_length=100)
#     location=models.CharField(null=True,blank=True,max_length=100)
#     def __str__(self):
#         return self.title

# class Category(models.Model):
#     name = models.CharField(max_length=100)

# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     priority = models.IntegerField(default=1)
#     description = models.TextField(default='')
#     location = models.CharField(max_length=255, default='')
#     organizer = models.CharField(max_length=100, default='')
    
    
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
