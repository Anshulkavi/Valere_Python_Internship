# blog/serializers.py

from rest_framework import serializers
from .models import CustomUser, Profile, Post, Tag, Category, Comment, Like

# --- Authentication and Profile Serializers ---

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data.get('full_name', ''),
            password=validated_data['password']
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    # These fields DO NOT exist on the Profile model itself.
    # They belong to the User model.
    id = serializers.ReadOnlyField(source='user.id')
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        # 'id', 'username', and 'email' are not part of the Profile model,
        # which causes the ProfileNestedSerializer to fail.
        fields = ('id', 'username', 'email', 'full_name', 'bio', 'profile_picture')

# --- Nested Serializers for Embedding in Other Serializers ---

class ProfileNestedSerializer(serializers.ModelSerializer):
    """ A simple serializer for nesting profile info inside the User. """
    class Meta:
        model = Profile
        fields = ['full_name', 'profile_picture']

class UserNestedSerializer(serializers.ModelSerializer):
    """ Serializer for nesting User info, including their profile. """
    profile = ProfileNestedSerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'profile']

# --- Main Content Serializers ---

class PostSerializer(serializers.ModelSerializer):
    author = UserNestedSerializer(read_only=True)
    tags = serializers.SlugRelatedField(
        many=True, slug_field='name', queryset=Tag.objects.all(), required=False
    )
    category = serializers.SlugRelatedField(
        slug_field='name', queryset=Category.objects.all(), allow_null=True, required=False
    )
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'featured_image', 'category', 'tags', 
            'created_at', 'author', 'likes_count', 'is_liked'
        ]

    def get_likes_count(self, obj):
        return obj.like.count()

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.like.filter(user=request.user).exists()
        return False

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.profile.full_name')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'user_id', 'user_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post']
        read_only_fields = ['id', 'user', 'post']