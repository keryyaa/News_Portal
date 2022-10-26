from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def rating_author(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        comRat = self.authorUser.comment_set.aggregate(comReting=Sum('rating'))
        cRat = 0
        cRat += comRat.get('comReting')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return f"Имя автора: {self.authorUser}, рейтинг: {self.ratingAuthor}"


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_POST = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )

    categoryTape = models.CharField(max_length=2, choices=CATEGORY_POST, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=256)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('posdetail', args=[str(self.id)])

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f"{self.text[:124]} ..."

    def __str__(self):
        return f"{self.title} : {self.text}"


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.postThrough} {self.categoryThrough}"


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


