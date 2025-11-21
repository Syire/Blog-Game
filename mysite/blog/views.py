
from django.views import generic as Generic
from django.shortcuts import render

from .models import Post

# Create your views here.
class PostList(Generic.ListView):
    queryset=Post.objects.filter(status=1).order_by('created_on')
    template_name='blog/index.html'

class PostDetail(Generic.DetailView):
    model=Post
    template_name='blog/post_detail.html'