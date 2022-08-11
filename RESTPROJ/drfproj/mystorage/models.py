from email.quoprimime import body_check
from multiprocessing import AuthenticationError
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.conf import settings

class Essay(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    body=models.TextField()

# Create your models here.
