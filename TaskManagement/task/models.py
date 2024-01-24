from django.db import models
from category.models import Category
# Create your models here.
class Task(models.Model):
    title =models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    category=models.ManyToManyField(Category)
    complete=models.BooleanField(default=False)
    date=models.DateField()

    def __str__(self):
        return self.title