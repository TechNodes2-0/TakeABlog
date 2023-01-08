from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from Auth.models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# Create your views here.

# def homepage(request):
#     return render(request, 'Core/homepage.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        Liked = False

    else:
        post.likes.add(request.user)
        Liked=True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))




class HomeView(ListView):
    model = Post
    template_name = 'homepage.html'
    ordering = ['-post_date']


class ArticleDetail(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class UpdatePostView(UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ['title', 'title_tag', 'body','profile_pic']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats.replace('-',' '), 'category_posts':category_posts})