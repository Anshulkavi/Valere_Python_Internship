from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser, OTP
from .serializers import (
    RegisterSerializer, VerifyOTPSerializer, LoginSerializer,
    ProfileSerializer, CompleteProfileSerializer
)
from datetime import timedelta
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from .utils import ( generate_otp,
        get_tokens_for_user, save_otp_to_redis,get_otp_from_redis,
        delete_otp_from_redis, can_resend_otp)
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from accounts.tasks import send_otp_email_task, send_welcome_email_task


@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp_code = generate_otp()
            # Clear any existing OTPs for this user
            # OTP.objects.filter(user=user).delete()
            # OTP.objects.create(user=user, code=otp_code)
            save_otp_to_redis(user.email, otp_code)
            send_otp_email_task.delay(user.email, user.username, otp_code)
            
            # Store email in session for OTP verification
            request.session['email'] = user.email
            request.session['user_id'] = user.id
            
            send_welcome_email_task.delay(user.email)

            return Response({
                'message': 'User registered successfully. OTP sent to your email.',
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class VerifyOTPView(APIView):
    def post(self, request):
        # Get email from session (registration flow) or request data (login flow)
        email = request.session.get('email') or request.data.get('email')
        otp = request.data.get('otp')

        if not email or not otp:
            return Response({
                'detail': 'Email and OTP are required'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({
                'detail': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)

        # try:
        #     otp_obj = OTP.objects.get(user=user, code=otp, is_used=False)
            
        #     # Check if OTP is expired (5 minutes)
        #     if timezone.now() - otp_obj.created_at > timedelta(minutes=5):
        #         otp_obj.delete()
        #         return Response({
        #             'detail': 'OTP has expired. Please request a new one.'
        #         }, status=status.HTTP_400_BAD_REQUEST)
                
        # except OTP.DoesNotExist:
        #     return Response({
        #         'detail': 'Invalid or expired OTP'
        #     }, status=status.HTTP_400_BAD_REQUEST)

        stored_otp = get_otp_from_redis(email)
        if stored_otp != otp:
            return Response({"detail": "Invalid or expired OTP"}, status=status.HTTP_400_BAD_REQUEST)

        # Mark email as verified
        user.is_email_verified = True
        user.save()
        
        # Mark OTP as used and delete it
        # otp_obj.is_used = True
        # otp_obj.save()
        # otp_obj.delete()
        delete_otp_from_redis(email)

        # Generate tokens
        tokens = get_tokens_for_user(user)
        
        # Clear session data
        if 'email' in request.session:
            del request.session['email']
        if 'user_id' in request.session:
            del request.session['user_id']

        return Response({
            'detail': 'Email verified successfully',
            'access': tokens['access'],
            'refresh': tokens['refresh'],
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_email_verified': user.is_email_verified,
                'is_profile_completed': user.is_profile_completed
            }
        }, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class ResendOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response({
                'detail': 'Email is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({
                'detail': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)

        if user.is_email_verified:
            return Response({
                'detail': 'Email is already verified'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # ⛔ Rate limit using Redis
        if not can_resend_otp(email):
            return Response({
                'detail': 'Please wait before resending OTP.'
            }, status=status.HTTP_429_TOO_MANY_REQUESTS)

        # ✅ Generate and store new OTP
        otp_code = generate_otp()
        save_otp_to_redis(user.email, otp_code)

        # ✅ Send email
        send_otp_email_task.delay(user.email, user.username, otp_code)
        
        # ✅ Optional: store email in session
        request.session['email'] = user.email

        return Response({
            'detail': 'New OTP sent to your email'
        }, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            
            # Check if email is verified
            if not user.is_email_verified:
                # Store email in session and return special response
                request.session['email'] = user.email
                return Response({
                    'detail': 'Email not verified',
                    'email': user.email,
                    'requires_verification': True
                }, status=status.HTTP_403_FORBIDDEN)
            
            # Generate tokens for verified users
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "is_email_verified": user.is_email_verified,
                    "is_profile_completed": user.is_profile_completed
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response({
                "message": "Logout successful"
            }, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({
                "error": "Invalid token"
            }, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


@method_decorator(csrf_exempt, name='dispatch')
class CompleteProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CompleteProfileSerializer(instance=request.user, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_profile_completed = True
            user.save()
            return Response({
                "detail": "Profile completed successfully.",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "full_name": user.full_name,
                    "phone_number": user.phone_number,
                    "is_email_verified": user.is_email_verified,
                    "is_profile_completed": user.is_profile_completed
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Template-based views
def onboarding_page(request):
    return render(request, "accounts/onboarding.html")


def Landing_page(request):
    return render(request, "accounts/landing.html")


def trigger_verify_view(request):
    """
    This view is called when a logged-in user needs to verify their email.
    It generates and sends an OTP, then redirects to the verification page.
    """
    # Check if user is logged in via session or token
    user = None
    
    # Try to get user from JWT token in session storage (handled by frontend)
    # For now, we'll handle this through the API endpoint
    
    # If called directly, redirect to login
    if not request.user.is_authenticated:
        return redirect('/login/')
    
    user = request.user
    
    # If already verified, redirect to profile
    if user.is_email_verified:
        return redirect('/profile/')
    
    # Generate and send OTP
    otp_code = generate_otp()
    OTP.objects.filter(user=user).delete()  # Clear old OTPs
    OTP.objects.create(user=user, code=otp_code)
    send_otp_email_task.delay(user.email,user.username, otp_code)
    
    # Store email in session for verification
    request.session['email'] = user.email
    
    return redirect('/otp/')


# API endpoint for sending OTP (used by frontend)
@method_decorator(csrf_exempt, name='dispatch')
class SendOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response({
                'detail': 'Email is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({
                'detail': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)

        # Generate and send OTP
        otp_code = generate_otp()
        OTP.objects.filter(user=user).delete()
        OTP.objects.create(user=user, code=otp_code)
        send_otp_email_task.delay(user.email,user.username,otp_code)
        
        # Store in session
        request.session['email'] = email

        return Response({
            'detail': 'OTP sent successfully'
        }, status=status.HTTP_200_OK)


