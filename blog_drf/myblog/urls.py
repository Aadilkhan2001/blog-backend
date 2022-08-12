from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet,LikesViewSet,CommentViewSet

router = DefaultRouter()

router.register(r'post',PostViewSet,basename='post')
router.register(r'comment',CommentViewSet,basename='comment')
router.register(r'likes',LikesViewSet,basename='likes')

urlpatterns = [
    path('',include(router.urls))
]
