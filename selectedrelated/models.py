from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)  
class Books(models.Model):
    book = models.CharField(max_length=30)
    author = models.ForeignKey(Author,related_name='auth_name',on_delete=models.CASCADE)
class store(models.Model):
    store_name = models.CharField(max_length=20)
    books = models.ManyToManyField(Books)
class banking(models.Model):
    user = models.CharField(max_length=20)
    balance = models.FloatField(default=0.0)


class Students(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    students = models.Manager()