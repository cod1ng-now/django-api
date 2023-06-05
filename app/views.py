from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import  Post
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import  Q

# Create your views here.



def error404(request, exception):
    return render(request,'404.html')
    
    
class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

class CreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'body']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'update.html'
    context_object_name = 'post'
    fields = ['title', 'body']


    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = "/"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user