from rest_framework.viewsets import ModelViewSet
from .models import Recipe, Tag
from .serializers import RecipeSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import CustomPagination

class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = CustomPagination  # Apply the custom pagination class
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # Add permissions

    # Enable search and filtering
    filter_backends = [SearchFilter, DjangoFilterBackend]

    # Search by title or ingredients
    search_fields = ['title', 'ingredients']

    # Filters for category and tags
    filterset_fields = ['category', 'tags']

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



# views.py
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


# views.py
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)