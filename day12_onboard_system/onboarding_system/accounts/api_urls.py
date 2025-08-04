# from django.urls import path
# from .views import RegisterView, LoginView, LogoutView, VerifyOTPView, ProfileView , CompleteProfileView,ResendOTPView,trigger_verify_view


# # print("RegisterView type:", type(RegisterViews))
# # print("RegisterView:", RegisterViews)
# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='api_register'),
#     path('login/', LoginView.as_view(), name='api_login'),
#     path('logout/', LogoutView.as_view(), name='api_logout'),
#     path('verify-otp/', VerifyOTPView.as_view(), name='api_otp'),
#     path('profile/', ProfileView.as_view(), name='api_profile'),
#     path('complete-profile/', CompleteProfileView.as_view(), name='api_complete_profile'),
#     path('resend-otp/', ResendOTPView.as_view(), name='resend_otp'),
#         path('trigger-verify/', trigger_verify_view, name='trigger_verify'),

# ]

from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView, VerifyOTPView, 
    ProfileView, CompleteProfileView, ResendOTPView, 
    SendOTPView, trigger_verify_view
)

urlpatterns = [
    # Authentication endpoints
    path('register/', RegisterView.as_view(), name='api_register'),
    path('login/', LoginView.as_view(), name='api_login'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
    
    # OTP endpoints
    path('verify-otp/', VerifyOTPView.as_view(), name='api_verify_otp'),
    path('resend-otp/', ResendOTPView.as_view(), name='api_resend_otp'),
    path('send-otp/', SendOTPView.as_view(), name='api_send_otp'),
    
    # Profile endpoints
    path('profile/', ProfileView.as_view(), name='api_profile'),
    path('complete-profile/', CompleteProfileView.as_view(), name='api_complete_profile'),
    
    # Trigger verify (for logged-in users)
    path('trigger-verify/', trigger_verify_view, name='api_trigger_verify'),
]