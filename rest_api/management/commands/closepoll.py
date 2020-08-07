import requests

from django.core.management.base import BaseCommand

from rest_api.models import Book


class Command(BaseCommand):
    help = 'Load JSON db'

    def handle(self, *args, **options):
        Book.objects.all().delete()
        response = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit').json()
        data = response['items']
        for i in range(len(data)):
            obj = Book.objects.create(
                id=data[i].get('id'),
                title=data[i].get('volumeInfo').get('title'),
                authors=data[i].get('volumeInfo').get('authors'),
                published_date=data[i].get('volumeInfo').get('publishedDate'),
                categories=data[i].get('volumeInfo').get('categories'),
                average_rating=data[i].get('volumeInfo').get('averageRating'),
                rating_count=data[i].get('volumeInfo').get('ratingCount'),
                thumbnail=data[i].get('volumeInfo').get('imageLinks').get('thumbnail'),
            )

            obj.save()

        self.stdout.write(self.style.SUCCESS('Successfully created db'))
