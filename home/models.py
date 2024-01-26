from django.db import models

# Create your models here.

class data(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()
    
    def __str__(self) -> str:
        return self.email