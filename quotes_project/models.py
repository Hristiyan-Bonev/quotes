from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    author_text = models.TextField(unique=True)

    def __str__(self):
        return self.author_text

    class Meta:
        db_table = 'authors'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_text = models.TextField(unique=True)

    def __str__(self):
        return self.category_text

    class Meta:
        db_table = 'categories'


class Quote(models.Model):
    quote_id = models.IntegerField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='author')
    quote = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category')
    likes = models.IntegerField(default=0)
    date_crawled = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'quote_data'

    def __str__(self):
        return self.quote


class DefaultUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email_address = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=False,
                                    verbose_name='account is activated')
    is_premium = models.BooleanField(default=False,
                                    verbose_name='account is a premium user')
    objects = UserManager()

    def __str__(self):
        return self.email_address
