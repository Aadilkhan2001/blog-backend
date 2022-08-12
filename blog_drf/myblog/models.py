from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError


# Create your models here.
class PostModels(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,unique=True)
    content = models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.title



class LikesModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(PostModels,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

 




class CommentModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(PostModels,on_delete=models.CASCADE)
    comment = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
