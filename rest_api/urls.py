from django.urls import path
from rest_framework import routers

from rest_api.api import BookView, PostBooksView, home_view

router = routers.SimpleRouter()
router.register(r'books', BookView, basename='books')
urlpatterns = [
    path('upload/', PostBooksView.as_view(), name='upload'),
    path('', home_view, name='home')
] + router.urls
