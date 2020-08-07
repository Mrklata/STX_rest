from rest_framework import routers
from rest_api.api import BookView


router = routers.SimpleRouter()
router.register(r'books', BookView, basename='book')
urlpatterns = router.urls
