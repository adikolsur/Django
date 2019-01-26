from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=128,unique=True)

    def __str__(self):
        return self.topic_name

class WebPage(models.Model):
    top=models.ForeignKey(Topic,on_delete=models.DO_NOTHING,)
    name=models.CharField(max_length=128,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.DO_NOTHING,)
    date=models.DateField()

    def __str__(self):
        return  str(self.date)

class User(models.Model):
    first_name=models.CharField(max_length=24)
    last_name=models.CharField(max_length=24)
    email=models.EmailField(max_length=128,unique=True)

    def __str__(self):
        return str(self.first_name+" "+self.last_name+" "+self.email)