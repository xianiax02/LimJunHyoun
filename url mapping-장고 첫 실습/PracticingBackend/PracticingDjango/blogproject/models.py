from pyexpat import model
from django.db import models

    class Blog(models.Model):
        title=models.CharField()
        body=models.TextField() 
        date=models.DateTimeField(auto_now_add=True)
        
        
# Create your models here.
