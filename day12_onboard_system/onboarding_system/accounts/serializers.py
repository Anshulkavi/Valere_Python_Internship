# # from rest_framework import serializers
# # from .models import CustomUser, OTP
# # from .utils import generate_otp
# # from django.contrib.auth import authenticate

# # class RegisterSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = CustomUser
# #         fields = ['username', 'password', 'email']
# #         extra_kwargs = {
# #             'password': {'write_only': True}
# #         }
    
# #     def create(self, validated_data):
# #         user = CustomUser.objects.create_user(
# #             username=validated_data['username'],
# #             email=validated_data['email'],
# #             password=validated_data['password']
# #         )
# #         return user


# # class VerifyOTPSerializer(serializers.Serializer):
# #     email = serializers.EmailField()
# #     otp = serializers.CharField()

# #     def validate(self, data):
# #        if not data.get('email'):
# #            raise serializers.ValidationError("Email is  required.")
# #        return data
    

# # class LoginSerializer(serializers.Serializer):
# #     username = serializers.CharField()
# #     password = serializers.CharField()

# #     def validate(self, data):
# #         username = data.get('username')
# #         password = data.get('password')

# #         if username and password:
# #             user = authenticate(username=username, password=password)
# #             if not user:
# #                 raise serializers.ValidationError("Invalid credentials")
# #             if not user.is_email_verified:
# #                 raise serializers.ValidationError("Email is not verified")
# #             data["user"] = user
# #             return data
# #         raise serializers.ValidationError("Must include username and password")
    

# # class ProfileSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = CustomUser
# #         fields = [
# #             'username',
# #             'email',
# #             'full_name',
# #             'phone_number',
# #             'is_email_verified',
# #             'is_profile_completed',
# #         ]

# #     def get_full_name(self, obj):
# #             return obj.full_name


# #     def update(self, instance, validated_data):
# #         instance.full_name = validated_data.get('full_name', instance.full_name)
# #         instance.phone_number = validated_data.get('phone_number', instance.phone_number)
# #         instance.is_profile_completed = True
# #         instance.save()
# #         return instance
    
# # class CompleteProfileSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = CustomUser
# #         fields = ['full_name', 'phone_number']

# from rest_framework import serializers
# from .models import CustomUser, OTP
# from django.contrib.auth import authenticate

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password', 'email']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         return CustomUser.objects.create_user(**validated_data)

# class VerifyOTPSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     otp = serializers.CharField()

#     def validate(self, data):
#         if not data.get('email'):
#             raise serializers.ValidationError("Email is required.")
#         return data

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(username=data['username'], password=data['password'])
#         if not user:
#             raise serializers.ValidationError("Invalid credentials")
#         if not user.is_email_verified:
#             raise serializers.ValidationError("Email is not verified")
#         data["user"] = user
#         return data

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = [
#             'username', 'email', 'full_name', 'phone_number',
#             'is_email_verified', 'is_profile_completed'
#         ]

#     def update(self, instance, validated_data):
#         instance.full_name = validated_data.get('full_name', instance.full_name)
#         instance.phone_number = validated_data.get('phone_number', instance.phone_number)
#         instance.is_profile_completed = True
#         instance.save()
#         return instance

# class CompleteProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['full_name', 'phone_number']

from rest_framework import serializers
from .models import CustomUser, OTP
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True, max_length=6, min_length=6)

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value

    def validate_otp(self, value):
        if not value or len(value) != 6 or not value.isdigit():
            raise serializers.ValidationError("OTP must be a 6-digit number.")
        return value


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Both username and password are required.")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        data["user"] = user
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'full_name', 'phone_number',
            'is_email_verified', 'is_profile_completed'
        ]
        read_only_fields = ['id', 'username', 'email', 'is_email_verified']

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        
        # Auto-mark profile as completed if both fields are provided
        if instance.full_name and instance.phone_number:
            instance.is_profile_completed = True
            
        instance.save()
        return instance


class CompleteProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True, max_length=100)
    phone_number = serializers.CharField(required=True, max_length=15)
    
    class Meta:
        model = CustomUser
        fields = ['full_name', 'phone_number']

    def validate_full_name(self, value):
        if not value or len(value.strip()) < 2:
            raise serializers.ValidationError("Full name must be at least 2 characters long.")
        return value.strip()

    def validate_phone_number(self, value):
        if not value or len(value.strip()) < 10:
            raise serializers.ValidationError("Please provide a valid phone number.")
        return value.strip()