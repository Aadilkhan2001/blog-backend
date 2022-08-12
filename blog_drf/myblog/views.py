from django.shortcuts import render
from rest_framework import viewsets
from .models import LikesModel, PostModels,CommentModel
from .serializers import PostSeializer,CommentSerializer,LikesSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .permissions import IsAuthorOrReadOnly,IsUserOrReadOnly
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSeializer
    queryset = PostModels.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)

    def update(self, request, *args, **kwargs):
        kwargs['partial']=True
        return super().update(request, *args, **kwargs)
  
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly,IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    def update(self, request, *args, **kwargs):
        kwargs['partial']=True
        return super().update(request, *args, **kwargs)

class LikesViewSet(viewsets.ModelViewSet):
    serializer_class = LikesSerializer
    queryset = LikesModel.objects.all()
    permission_classes=[IsAuthenticated,IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
    