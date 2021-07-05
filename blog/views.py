from django.db import models
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.


class BlogListView(ListView):

    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):  # this view spect a pk or a slugname cos... is detail

    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):

    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):

    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):

    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
