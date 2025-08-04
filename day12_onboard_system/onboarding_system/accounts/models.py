# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils import timezone
# from datetime import timedelta

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True, blank=False, null=False, default="user@example.com")
#     full_name = models.CharField(max_length=100, blank=True,null=False)
#     phone_number = models.CharField(max_length=15, blank=True,null=True)
#     is_email_verified = models.BooleanField(default=False)
#     is_profile_completed = models.BooleanField(default=False)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username

# class OTP(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='otps')
#     code = models.CharField(max_length=6)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_used = models.BooleanField(default=False)

#     def __str__(self):
#         return f"OTP {self.code} for {self.user.username}"
    
#     def is_expired(self):
#         """Check if OTP is expired (5 minutes)"""
#         return timezone.now() - self.created_at > timedelta(minutes=5)
    
#     class Meta:
#         ordering = ['-created_at']

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        default="user@example.com",
        help_text="User's unique email address"
    )
    full_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="User's full name"
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        help_text="Optional phone number"
    )
    is_email_verified = models.BooleanField(default=False)
    is_profile_completed = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class OTP(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='otps',
        help_text="User to whom the OTP belongs"
    )
    code = models.CharField(
        max_length=6,
        help_text="6-digit OTP code"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Time when the OTP was created"
    )
    is_used = models.BooleanField(
        default=False,
        help_text="Flag indicating if the OTP has been used"
    )

    def __str__(self):
        return f"OTP(code={self.code}, user={self.user.username}, used={self.is_used})"

    def is_expired(self):
        """Check if OTP is expired (valid for 5 minutes only)"""
        return timezone.now() - self.created_at > timedelta(minutes=5)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "OTP"
        verbose_name_plural = "OTPs"
