from django.utils.datetime_safe import datetime
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import PostCreate
from .filters import PostFilter
from django.contrib.auth.mixins import PermissionRequiredMixin


# Создаем класс для вывода всех новостей из бд наследуемся от ListView
class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'PostList.html'
    context_object_name = 'PostList'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


# Создаем класс для вывода одиночной новости по ее ID в данном случае наследуемся от DetailView
class PosDetail(DetailView):
    model = Post
    template_name = 'PostDetail.html'
    context_object_name = 'PostDetail'


class CreatePost(PermissionRequiredMixin, CreateView):
    permission_required = ('news_one.add_post')
    form_class = PostCreate
    model = Post
    template_name = 'createPost.html'
    success_url = "/news/"


# Представление редактирования постов
class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news_one.change_post')
    form_class = PostCreate
    model = Post
    template_name = 'createPost.html'
    success_url = "/news/"


# Создаем представление удаления постов
class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news_one.delete_post')
    model = Post
    template_name = 'PostDelete.html'
    success_url = '/news/'


# представление поисковика
class PostCategoryListSearch(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'PostSearch.html'
    context_object_name = 'PostSearch'

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context
