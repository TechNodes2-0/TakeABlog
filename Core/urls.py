from django.contrib import admin
from django.urls import path, include
# from . import views
from .views import HomeView, ArticleDetail, AddPostView, UpdatePostView, CategoryView,LikeView

urlpatterns = [
    # path('', views.homepage, name ="homepage"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit_post/<int:pk>', UpdatePostView.as_view(), name="edit_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name='like_post')

]