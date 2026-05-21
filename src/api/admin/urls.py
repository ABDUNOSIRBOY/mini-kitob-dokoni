from django.urls import path, include
from api.admin.views import category_views, author_views, book_views
from rest_framework.routers import DefaultRouter

r = DefaultRouter()

r.register("category", category_views.CategoryViewSet, basename="categoryviews")
r.register("author", author_views.AuthorViewSet, basename="authorviews")
r.register("book", book_views.BookViewSet, basename="bookviews")


urlpatterns = [
    path('', include(r.urls)),
]