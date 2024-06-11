from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    author_User = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_Author = models.IntegerField(default=0)

    def update_rating(self):
        post_rat = Post.objects.filter(author=self).aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += post_rat.get('postRating')

        comment_rat = Comment.objects.filter(comment_post__author=self).aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += comment_rat.get('commentRating')

        self.rating_Author = pRat*3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICE = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOICE, default=ARTICLE)
    date_create = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    objects = models.Manager()

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

    def __str__(self):
        return f"{self.title}: {self.text[:20]}"

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    objects = models.Manager()

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
