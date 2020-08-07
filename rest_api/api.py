import requests
from django.shortcuts import render
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_api.models import Book
from rest_api.serializers import BookSerializer


class BookView(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    parser_classes = [JSONParser]
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'
    filter_fields = ['title', 'authors', 'published_date']
    ordering = ['id']

    def get_queryset(self):

        return Book.objects.all()

    def get_book_id(self):
        return Book.objects.filter(pk=self.kwargs['id'])


class PostBooksView(APIView):
    model = Book
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FileUploadParser]

    def post(self, request, format=None):
        Book.objects.all().delete()
        response = requests.get('https://www.googleapis.com/books/v1/volumes?q=war').json()
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

        return Response(status=204)


def home_view(request):
    return render(request, 'rest_api/home.html')
