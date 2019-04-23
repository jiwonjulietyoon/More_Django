from django.shortcuts import render

from django.conf import settings
from .models import Post
from .forms import PostForm



# Create your views here.
def create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        unsaved_post = form.save(commit=False)
        unsaved_post.user_id = 1
        unsaved_post.save()