import json
from abc import ABC

import requests

from django.core.management.base import BaseCommand

from rest_api.models import Book


class Command(BaseCommand):
    help = 'Load JSON db'

    def handle(self, *args, **options):
        response = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit').json()
        data = response['items']
        for i in range(len(data)):
            obj = Book.objects.create(data)
            obj.save()

        self.stdout.write(self.style.SUCCESS('Successfully created db'))

