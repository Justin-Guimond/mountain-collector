from django.db import models

# Create your models here.
class Mountain(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    datehiked = models.DateField()
    elevation = models.IntegerField() 

    

