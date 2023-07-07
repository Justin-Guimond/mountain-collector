from django.db import models
from django.urls import reverse

# Create your models here.
class Mountain(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    datehiked = models.DateField()
    elevation = models.IntegerField() 

# Changing this instance method
# does not impact the database, therefore
# no makemigrations is necessary
    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'mountain_id': self.id})



