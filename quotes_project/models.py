from django.db import models


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
    id = models.IntegerField(primary_key=True)  # AutoField?
    quote_text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category')
    scraped_date = models.TextField()
    is_favourite = models.IntegerField()
    was_qod = models.IntegerField()

    def __str__(self):
        return self.quote_text

    class Meta:
        managed = False
        db_table = 'quote_data'
