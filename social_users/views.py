from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *


def index(request):
    return HttpResponse("hello users")


class CreatePost(CreateView):
    model = Posts
    fields = ['Post_Image', 'Caption']
    success_url = reverse_lazy('social_user:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)


class UpdatePost(UpdateView):
    model = Posts
    fields = ['Post_Image', 'Caption']
    success_url = reverse_lazy('social_user:index')


class PostList(ListView):
    model = Posts
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user=self.request.user)
        return context


class PostDetails(DetailView):
    model = Posts
    context_object_name = 'posts'


class PostDelete(DeleteView):
    model = Posts
    context_object_name = 'post'
    success_url = reverse_lazy('social_user:post_list')
