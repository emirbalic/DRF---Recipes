from rest_framework import serializers
from .models import Recipe, Category, Tag


# serializers.py
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


# serializers.py
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Customize this based on the fields you want to return

class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    created_by = UserSerializer()  # Nested UserSerializer for the created_by field

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'ingredients', 'instructions', 'category', 'tags', 'created_by', 'created_at', 'updated_at']
        # fields = '__all__'

        
        # fields = ['title', 'description', 'ingredients']

