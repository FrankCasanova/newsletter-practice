from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class BlogListView(ListView):

    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):  # this view spect a pk or a slugname cos... is detail

    model = Post
    template_name = 'post_detail.html'
