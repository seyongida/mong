from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
            return self.content
        
        
class Board(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    writer = models.CharField(max_length=20, null=True)
    
class Board2(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    
class Board3(models.Model):
    title = models.CharField(max_length=40, null=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    
    def __str__(self):
        return self.title