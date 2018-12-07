from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    author = models.TextField(unique=True)

    def __str__(self):
        return self.author

    class Meta:
        managed = False
        db_table = 'authors'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category = models.TextField(unique=True)

    def __str__(self):
        return self.category

    class Meta:
        managed = False
        db_table = 'categories'


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category')
    id = models.IntegerField(primary_key=True)
    is_favourite = models.IntegerField()
    was_qod = models.IntegerField()
    likes = models.IntegerField()
    quote_text = models.TextField()
    scraped_date = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote_text

    class Meta:
        managed = False
        db_table = 'quote_data'


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
        return self.username
