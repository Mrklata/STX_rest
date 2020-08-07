import json
import requests

from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, filters

from rest_api.models import Book
from rest_api.serializers import BookSerializer


class BookView(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'
    filter_fields = ['title', 'authors', 'published_date']
    ordering = ['id']

    def get_queryset(self):

        return Book.objects.all()

    def get_book_id(self):
        return Book.objects.filter(pk=self.kwargs['id'])

    def perform_create(self, serializer):
        # response = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit').json()
        # data = response
        # objects = Book.objects.create(
        #     id=data['id'],
        #     title=data['title'],
        #     authors=data['authors'],
        #     published_date=data['published_date'],
        #     categories=data['categories'],
        #     average_rating=['average_rating'],
        #     rating_count=['rating_count'],
        #     thumbnail=['thumbnail']
        # )
        return serializer.save()
