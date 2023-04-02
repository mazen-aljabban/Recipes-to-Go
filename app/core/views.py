from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from django.db.models.aggregates import Count
from .models import *
from .serializers import *
from .permissions import IsCreatorOrReadOnly, IsAdminOrReadOnly


class ChefViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
    permission_classes = [IsCreatorOrReadOnly]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.user.is_anonymous:
            raise PermissionDenied({'message': 'Unauthorized user. Please log in to continue.'})
        return [IsCreatorOrReadOnly()]
    
    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        if not request.user.is_authenticated:
            return Response(status.HTTP_404_NOT_FOUND)
        (chef, created) = Chef.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = ChefSerializer(chef)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = ChefSerializer(chef, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
        
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(recipes_count=Count('recipes')).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def destroy(self, request, *args, **kwargs):
        if Recipe.objects.filter(collection_id=kwargs['pk']):
            return Response({'error': 'Collection cannot be deleted because it includes one or more Recipes.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, **kwargs)
    
    
class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        if Recipe.objects.filter(collection_id=kwargs['pk']):
            return Response({'error': 'Collection cannot be deleted because it is assigned to one or more Recipes.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, **kwargs)
    
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(collections_count=Count('collections')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
    
class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.user.is_anonymous:
            raise PermissionDenied({'message': 'Unauthorized user. Please log in to continue.'})
        return [IsCreatorOrReadOnly()]
    
    
    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to a recipe"""
        recipe = self.get_object()
        serializer = self.get_serializer(
            recipe,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )