from rest_framework.viewsets import ModelViewSet
from apps.kitob.models import Category
from api.admin.serializer.category_serializers import CategorySerializer




class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
