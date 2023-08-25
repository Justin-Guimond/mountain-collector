from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Mountain(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    datehiked = models.DateField()
    elevation = models.IntegerField() 
    # add user_id FK column
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Changing this instance method
# does not impact the database, therefore
# no makemigrations is necessary
    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'mountain_id': self.id})



