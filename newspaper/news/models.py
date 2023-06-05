from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingauthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        pass


Politice = 'Политика'
Sport = 'Спорт'
Education = 'Образование'

CATEGORY = [
    (Politice, 'Политика'),
    (Sport, 'Спорт'),
    (Education, 'Образование'),
]


class Category(models.Model):
    category = models.CharField(max_length=64,
                                choices=CATEGORY,
                                default=Education,
                                unique=True)


Article = 'Ar'
News = 'Nw'

NEAR = [
    (Article, 'Статья'),
    (News, 'Новость')
]


class Post(models.Model):
    post_type = models.CharField(max_length=2, choices=NEAR, default=News)
    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    headerPost = models.CharField(max_length=256)
    textPost = models.TextField()
    createPost = models.DateTimeField(auto_now_add=True)
    raitPost = 0
    categoryes = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        pass

    def dislike(self):
        pass

    def previec(self):
        pass


class Comment(models.Model):
    PostComment = models.ForeignKey(Post, on_delete=models.CASCADE)
    CommentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    textComment = models.TextField()
    commentcreate = models.DateField(auto_created=True)
    rateComment = 0


class PostCategory(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThough = models.ForeignKey(Category, on_delete=models.CASCADE
                                       )