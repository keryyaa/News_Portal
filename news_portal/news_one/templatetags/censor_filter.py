from django import template

register = template.Library()
# Регестрируем фильтр для плохих слов
@register.filter()
def censor_text(text):
    # Создаем список слов которые мы не хотим видеть в наших статьях
    # Я бы создал его в БД с возвожностью добовления новых слов
    wanted_words = ['редиска', 'помидор', 'бмв', 'готовить', 'масло']

    # Проверяем наш текст на принадлежность к str:
    # Если не проходит выбрасываем ошибку TypeError
    if not isinstance(text, str):
        raise TypeError(f"Данный тип обьекта {text}, не принадлежит типу данных 'str'")

    # разбиваем текст по словам и проходимся циклом если находится такое слово то которое есть в словаре заменяем его
    for _ in text.split():
        if _.replace('.','').lower() in wanted_words:
            text = text.replace(_, f'{_[0]}{"*" * (len(_) - 1)}')
    return f"{text}"
