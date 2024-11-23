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

# class RecipeSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     tags = TagSerializer(many=True)
#     created_by = UserSerializer()  # Nested UserSerializer for the created_by field

#     class Meta:
#         model = Recipe
#         fields = ['id', 'title', 'description', 'ingredients', 'instructions', 'category', 'tags', 'created_by', 'created_at', 'updated_at']
#         # fields = '__all__'
"""but for the update I need"""

# class RecipeSerializer(serializers.ModelSerializer):
#     # Use PrimaryKeyRelatedField to accept IDs for related fields
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
#     created_by = serializers.PrimaryKeyRelatedField(read_only=True)  # Prevent overwriting creator

#     class Meta:
#         model = Recipe
#         fields = ['id', 'title', 'description', 'ingredients', 'instructions', 'category', 'tags', 'created_by', 'created_at', 'updated_at']

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'ingredients', 'instructions',
            'category', 'tags', 'created_by', 'created_at', 'updated_at'
        ]

    def to_representation(self, instance):
        # Dynamically set nested serializers for the response
        self.fields['category'] = CategorySerializer(read_only=True)
        self.fields['tags'] = TagSerializer(many=True, read_only=True)
        self.fields['created_by'] = UserSerializer(read_only=True)
        return super().to_representation(instance)

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(write_only=True, default=False)  # Allow passing `is_staff`

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']

    def validate_is_staff(self, value):
        """
        Only superusers or staff can create staff accounts.
        """
        user = self.context['request'].user
        if value and (not user.is_authenticated or not user.is_staff):
            raise serializers.ValidationError("You do not have permission to create staff users.")
        return value

    def create(self, validated_data):
        is_staff = validated_data.pop('is_staff', False)  # Default to False if not provided
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        user.is_staff = is_staff  # Set staff status
        user.save()
        return user