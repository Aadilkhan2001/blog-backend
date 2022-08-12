from django.contrib import admin
from .models import PostModels,LikesModel,CommentModel
# Register your models here.


@admin.register(PostModels)
class PostModelsAdmin(admin.ModelAdmin):
    list_display= ['author','title','content','created_date']

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','post','comment','posted_at']

@admin.register(LikesModel)
class LikeAdmin(admin.ModelAdmin):
    list_displa = ['user','post']

