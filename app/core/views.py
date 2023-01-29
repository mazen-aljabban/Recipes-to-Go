from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import *
from .serializers import ChefSerializer


class ChefViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        """Will allow anyone to see the chefs but only authenticated can update """
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    
    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        (chef, created) = Chef.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = ChefSerializer(chef)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = ChefSerializer(chef, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)