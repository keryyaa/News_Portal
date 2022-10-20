
from .models import Post
from django.views.generic import ListView, DetailView


# Создаем класс для вывода всех новостей из бд наследуемся от ListView
class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'PostList.html'
    context_object_name = 'PostList'


# Создаем класс для вывода одиночной новости по ее ID в данном случае наследуемся от DetailView
class PosDetail(DetailView):
    model = Post
    template_name = 'PostDetail.html'
    context_object_name = 'PostDetail'
