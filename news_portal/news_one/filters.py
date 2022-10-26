from django_filters import FilterSet, ModelChoiceFilter,  DateFilter
from .models import Post, Category
from django import forms


# Cоздаем поиск по сайту
class PostFilter(FilterSet):
    # поиск по категории
    category = ModelChoiceFilter(
        field_name='postCategory',
        queryset= Category.objects.all(),
        label='Категории',
        empty_label='Все категории',
    )

    #  поиск по дате
    date = DateFilter(
        field_name='dateCreation',
        lookup_expr='lt',
        widget=forms.DateInput(format='%m /%d /%Y',
                               attrs={'type': 'date'},
                               ),
        label='Выберете дату:'
    )

    # поиск по заголовку
    class Meta:
        model = Post
        fields = {
            'title': ['exact'],
        }