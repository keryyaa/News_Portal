from django.urls import path
from .views import PostList, PosDetail

urlpatterns = [
    # При переходе на /news будет выводиться всь список новостей
    path('', PostList.as_view()),

    # При переходе на /news/'номер id' будет выводиться новость по ее id
    path('<int:pk>', PosDetail.as_view()),
]
