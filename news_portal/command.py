''''

# Создаем пользоватей User так как модель Author имеет связь OneToOne с  User в authorUser:
u1 = User.objects.create_user(username='Max')).
u2 = User.objects.create_user(username='Andre')).

# Создаем двух авторов:
Author.objects.create(authorUser=u1)
Author.objects.create(authorUser=u2)

# Еще один способ записать то что писали выше:
Author.objects.create(authorUser=User.objects.create_user(username=Max)))
Author.objects.create(authorUser=User.objects.create_user(username=Andre)))

# Добавляем категории:
Category.objects.create(name=IT)
Category.objects.create(name=Avto)
Category.objects.create(name=Moto)
Category.objects.create(name=Instrument)

# Добавляем посты:
Post.objects.create(author=Author(1), categoryTape='NW', title='Кому на руси жить хорошо!', text='Ивану на печи жить было точно хорошо')
Post.objects.create(author=Author(2), categoryTape='AR', title='Почему русские любят рыбалку?', text='Русские любят рыбалку пптому что она душу греет')
Post.objects.create(author=Author(1), categoryTape='AR', title='Новые авто БМВ!', text='Новые авто БМВ будут собираться на автозаводе Лада и называться БМВАЗ')

# Присваиваем категории к постам:
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=4))

Или же еще есть возможность добавить таким образом:
PostCategory.objects.create(postThrough=Post.objects.get(id=1), categoryThrough=Category.objects.get(id=4))
и так далее.

# Создаем комментарии к постам:
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='Класс')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='Супер')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='Отлично')
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='Хорошо')

# Применяем функции like() и dislike() к статьям/новостям и комментариям:
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).dislike
Comment.objects.get(id=3).dislike
Comment.objects.get(id=4).dislike
Post.objects.get(id=1).like()
Post.objects.get(id=2).like()
Post.objects.get(id=3).like()
Post.objects.get(id=1).like()
Post.objects.get(id=2).dislike
Post.objects.get(id=3).dislike

#Обновляем рейтинги пользователей:
Author.objects.get(id=1).rating_author()
Author.objects.get(id=2).rating_author()

# Выводим рейтинг лучшего пользователя:
Данный код будет работать есть в классе Autor есть функция __str__:
Author.objects.order_by('-ratingAuthor')[:1]

Если нету но необходимо пройтись по обьекту QuerySet циклом будет выглядеть таким образом:
author=Author.objects.order_by('-ratingAuthor')[:1]
for _ in author:
    _.authorUser.username
    _.ratingAuthor

# Выводим дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
a = Post.objects.order_by('-rating')[:1]
for i in a:
    i.dateCreation
     i.author
     i.rating
     i.title
     i.preview()


#
Используем objects.filter для того что бы получить QuerySet:
Иначе будет ошибка так как возращаемых обьектов больше 1.
a = Comment.objects.filter(commentPost=Post.objects.order_by('-rating')[:1])
 for _ in a:
    _.dateCreation
    _.commentUser.username
    _.rating
    _.text

'''
