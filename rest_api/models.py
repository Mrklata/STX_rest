from django.db import models


class Book(models.Model):

    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    authors = models.CharField(max_length=200, blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    categories = models.CharField(max_length=200, blank=True, null=True)
    average_rating = models.IntegerField(blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f"{self.title} by {self.authors}"
