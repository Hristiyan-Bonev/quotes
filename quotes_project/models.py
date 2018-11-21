from django.db import models


class Authors(models.Model):
    author_id = models.IntegerField(primary_key=True)
    author = models.TextField(unique=True)

    def __str__(self):
        return self.author

    class Meta:
        managed = False
        db_table = 'authors'


class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category = models.TextField(unique=True)

    def __str__(self):
        return self.category

    class Meta:
        managed = False
        db_table = 'categories'


class QuoteData(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    quote_text = models.TextField()
    author = models.ForeignKey(Authors, models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='category')
    scraped_date = models.TextField()
    is_favourite = models.IntegerField()
    was_qod = models.IntegerField()

    def __str__(self):
        return self.quote_text

    class Meta:
        managed = False
        db_table = 'quote_data'
