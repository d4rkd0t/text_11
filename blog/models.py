from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_birth = models.DateField()
    rationg = (
    (1, "Worst"),
    (2, "Bad"),
    (3, "Not Bad"),
    (4, "Good"),
    (5, "Excellent!"),
    )
    
    num_stars = models.IntegerField(choices=rationg)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
class data(models.Model):
    full_name = models.ForeignKey(info, on_delete=CASCADE)
    user_name = models.CharField(max_length=50)
    user_number = models.CharField(max_length=11)
    user_bio = models.TextField(max_length=300)
    
    def __str__(self):
        return self.user_name
    