# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser, OTP
# # Register your models here.

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'is_email_verified', 'is_profile_completed', 'is_staff')
#     list_filter = ('is_email_verified', 'is_profile_completed','is_staff', 'is_superuser')
#     search_fields = ('username', 'email', 'phone_number')
#     ordering = ('-date_joined',)

#     fieldsets = UserAdmin.fieldsets + (
#         ('Verification Info', {
#             'fields': ('is_email_verified', 'is_profile_completed', 'phone_number'),
#         }),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#     ('Additional Info', {
#         'fields': ('phone_number',),
#     }),
# )



# @admin.register(OTP)
# class OTPAdmin(admin.ModelAdmin):
#     list_display = ('user', 'code', 'created_at', 'is_used')
#     list_filter = ('is_used', 'created_at')
#     search_fields = ('user__username', 'user__email', 'code')
#     ordering = ('-created_at',)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, OTP

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_email_verified', 'is_profile_completed', 'date_joined')
    list_filter = ('is_email_verified', 'is_profile_completed', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'full_name')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('full_name', 'phone_number', 'is_email_verified', 'is_profile_completed')
        }),
    )

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'created_at', 'is_used', 'is_expired_display')
    list_filter = ('is_used', 'created_at')
    search_fields = ('user__username', 'user__email', 'code')
    readonly_fields = ('created_at',)
    
    def is_expired_display(self, obj):
        return obj.is_expired()
    is_expired_display.boolean = True
    is_expired_display.short_description = 'Expired'