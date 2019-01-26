from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=24)
    last_name=models.CharField(max_length=24)
    email=models.EmailField(max_length=128,unique=True)

    def __str__(self):
        return str(self.first_name+" "+self.last_name+" "+self.email)