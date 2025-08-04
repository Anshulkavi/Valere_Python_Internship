from django.urls import path
from .views import onboarding_page
from django.views.generic import TemplateView

urlpatterns = [
    # Template pages
    path('register/', TemplateView.as_view(template_name='accounts/register.html'), name='register'),
    path('login/', TemplateView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('otp/', TemplateView.as_view(template_name='accounts/verify-otp.html'), name='verify_otp'),
    path('logout/', TemplateView.as_view(template_name='accounts/logout.html'), name='logout_page'),
    path('complete-profile/', TemplateView.as_view(template_name='accounts/complete-profile.html'), name='complete_profile'),
    # path('', TemplateView.as_view(template_name='accounts/onboarding.html'), name='onboard'),
    path('', TemplateView.as_view(template_name='accounts/landing.html'), name='landing'),

]

