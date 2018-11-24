from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True)
    #time = models.TextField(null=True)
    def __str__(self):
        return self.title
    #D:\APP\work\Anaconda3\python