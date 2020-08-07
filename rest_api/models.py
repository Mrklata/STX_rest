from django.db import models


class Book(models.Model):

    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)
    categories = models.CharField(max_length=200)
    average_rating = models.IntegerField()
    rating_count = models.IntegerField()
    thumbnail = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f"{self.title} by {self.authors}"
