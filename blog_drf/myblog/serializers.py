from .models import PostModels,LikesModel,CommentModel
from rest_framework import serializers


class PostSeializer(serializers.ModelSerializer):
    comments  =  serializers.SerializerMethodField(read_only = True)
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PostModels
        fields = ['title','author','content','comments','likes']
        read_only_fields = (['author'])
    
    def get_likes(self,obj):
        total_likes = LikesModel.objects.filter(post=obj.id).count()
        return total_likes

    def get_comments(self,obj):
        query_set = CommentModel.objects.filter(post=obj.id)
        serializer = CommentSerializer(query_set,many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = CommentModel
        fields = ['user','comment','post','posted_at']
        read_only_fields = (['user','posted_at'])


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesModel
        fields=['user','post']
        read_only_fields = (['user'])



