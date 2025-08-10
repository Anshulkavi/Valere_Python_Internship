import random
# from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
import redis
from django.conf import settings


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def generate_otp():
    return str(random.SystemRandom().randint(100000, 999999))

# def send_otp_email(user, otp_code):
#     html_message = f"""
#     <html>
#       <body style="font-family: Arial, sans-serif; line-height: 1.6;">
#         <h2 style="color: #2c3e50;">Welcome to Our Platform!</h2>
#         <p>Hi <strong>{user.username}</strong>,</p>
#         <p>Your OTP for email verification is:</p>
#         <h1 style="color: #e74c3c;">{otp_code}</h1>
#         <p>This OTP is valid for <strong>5 minutes</strong>.</p>
#         <p>If you did not initiate this request, you can safely ignore this message.</p>
#         <br>
#         <p style="color: #7f8c8d;">Thanks,<br>The Team</p>
#       </body>
#     </html>
#     """

#     send_mail(
#         subject="Verify Your Email - OTP Inside",
#         message=f"Your OTP is {otp_code}",
#         from_email=None,  # Will use DEFAULT_FROM_EMAIL from settings.py
#         recipient_list=[user.email],
#         fail_silently=False,
#         html_message=html_message
#     )

redis_client = redis.Redis(
    host='redis',
    port=6379,
    db=0,
    decode_responses=True  # So you get string values
)

def save_otp_to_redis(email, otp):
    redis_client.setex(f"otp:{email}", 300, otp)  #expires in 5mins

def get_otp_from_redis(email):
    otp = redis_client.get(f"otp:{email}")
    return otp.decode() if otp else None

def delete_otp_from_redis(email):
    redis_client.delete(f"otp:{email}")

def can_resend_otp(email):
    key = f"otp:resend_limit:{email}"
    if  redis_client.exists(key):
        return False
    redis_client.setex(key, 60, "1") #cooldown for 60 secs
    return True