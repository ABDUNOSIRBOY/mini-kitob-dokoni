from django.urls import path, include
from api.admin.views import cotegory_views, auth_views, book_views
from rest_framework.routers import DefaultRouter

r = DefaultRouter()

r.register("category", cotegory_views.CategoryViewSet, basename="categoryviews")
r.register("author", auth_views.AuthorViewSet, basename="authviews")
r.register("book", book_views.BookViewSet, basename="bookviews")


urlpatterns = [
    path('', include(r.urls)),
]