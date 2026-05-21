from rest_framework.viewsets import ModelViewSet
from apps.kitob.models import Author
from api.admin.serializer.author_serializers import AuthorSerializer




class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
