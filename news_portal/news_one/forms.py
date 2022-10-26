from django import forms
from django.core.exceptions import ValidationError
from .templatetags import censor_filter
from .models import Post



# Создаем форму оформления новостей
class PostCreate(forms.ModelForm):
    class Meta:
       model = Post
       fields = [
           'author',
           'categoryTape',
           'postCategory',
           'title',
           'text',
       ]
    # Делаем собственный фильтр по тексту что бы он был не менее 20 сивмволов и не совпадал с заголовком
    def clean(self):
        # Проверка на длину текста
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 20:
            raise ValidationError({
                "description": "Описание не может быть менее 20 символов."
            })
        # проверка на идентичность с заголовком
        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )


        return cleaned_data