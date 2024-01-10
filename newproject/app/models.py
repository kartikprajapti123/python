from django.db import models
from datetime import datetime
# Create your models here.
class genre(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Movie(models.Model):
    title=models.CharField(max_length=100)
    release_yeat=models.IntegerField()
    number_in_stock=models.IntegerField()
    daily_rate=models.FloatField()
    genre1=models.ForeignKey(genre,on_delete=models.CASCADE,related_name="abc")
    
    date=models.CharField(default=datetime.now(),max_length=100)
    
    def __str__(self):
        return self.title