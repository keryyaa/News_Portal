from django.contrib import admin
from .models import Post, Category, Comment, Author

# Регистрируем модели что-бы увидеть их в админ панели
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Author)


# Register your models here.
