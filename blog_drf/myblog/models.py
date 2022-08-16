from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError


# Create your models here.
class PostModels(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LikesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModels, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def save(self, *args,**kwargs):
        user = User.objects.get(id=self.user.id)
        post = PostModels.objects.get(id=self.post.id)
        try:
            check = LikesModel.objects.get(user=user,post=post)
        except LikesModel.DoesNotExist:
            self.liked = True
            super().save(self,*args, **kwargs)
        else:
            raise  ValidationError("Only one like allow!!")
                





class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModels, on_delete=models.CASCADE)
    comment = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
