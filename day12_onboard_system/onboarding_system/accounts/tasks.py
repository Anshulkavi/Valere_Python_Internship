from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email_task(email):
    print(f"Sending welcome email to {email}")
    return f"Email sent to {email}"

@shared_task
def send_otp_email_task(email,username, otp_code):
    html_message = f"""
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <h2 style="color: #2c3e50;">Welcome to Our Platform!</h2>
        <p>Hi <strong>{username}</strong>,</p>
        <p>Your OTP for email verification is:</p>
        <h1 style="color: #e74c3c;">{otp_code}</h1>
        <p>This OTP is valid for <strong>5 minutes</strong>.</p>
        <p>If you did not initiate this request, you can safely ignore this message.</p>
        <br>
        <p style="color: #7f8c8d;">Thanks,<br>The Team</p>
      </body>
    </html>
    """

    send_mail(
        subject="Verify Your Email - OTP Inside",
        message=f"Your OTP is {otp_code}",
        from_email=None,  # Will use DEFAULT_FROM_EMAIL from settings.py
        recipient_list=[email],
        fail_silently=False,
        html_message=html_message
    )

@shared_task
def debug_task():
    print("Celery is working!")
    return "Success"