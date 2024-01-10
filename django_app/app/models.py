from django.db import models

# Create your models here.
class singer(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class song(models.Model):
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    duration=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name