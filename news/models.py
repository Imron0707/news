from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingauthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.author.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingauthor = pRat * 3 + cRat
        self.save()


Politice = 'Политика'
Sport = 'Спорт'
Education = 'Образование'
IT = 'IT'
CITY = 'Город'

CATEGORY = [
    (Politice, 'Политика'),
    (Sport, 'Спорт'),
    (Education, 'Образование'),
    (IT, 'IT'),
    (CITY, 'Город'),
]


class Category(models.Model):
    name = models.CharField(max_length=64,
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
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    headerPost = models.CharField(max_length=256)
    textPost = models.TextField()
    createPost = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)
    categoryes = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        pass

    def dislike(self):
        pass

    def previev(self):
        return '{} ... {}'.format(self.textPost[0:123], str(self.rating))  # Поменять на F строки


class Comment(models.Model):
    PostComment = models.ForeignKey(Post, on_delete=models.CASCADE)
    CommentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    textComment = models.TextField()
    commentcreate = models.DateField(auto_created=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThough = models.ForeignKey(Category, on_delete=models.CASCADE)
