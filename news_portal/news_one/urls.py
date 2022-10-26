from django.urls import path
from .views import PostList, PosDetail, CreatePost, PostCategoryListSearch, PostUpdate, PostDelete

urlpatterns = [
    # При переходе на /news будет выводиться всь список новостей
    path('', PostList.as_view()),

    # При переходе на /news/'номер id' будет выводиться новость по ее id
    path('<int:pk>', PosDetail.as_view()),
    # путь на для поисковика
    path('search/', PostCategoryListSearch.as_view()),
    # путь создания поста
    path('create/', CreatePost.as_view(), name='post_create'),
    # путь редактирования поста
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    # путь удаления поста
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
