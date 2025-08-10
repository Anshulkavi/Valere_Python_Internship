from celery import shared_task
from django.core.mail import send_mail
from smtplib import SMTPException
import time
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=10)
def send_welcome_email_task(self,email):
    subject = "Welcome to Our Platform!"
    message = (
        "Thanks for registering with us!\n\n"
        "We're excited to have you on board.\n\n"
        "Regards,\nThe Team"
    )

    html_message = f"""
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <h2 style="color: #2c3e50;">Welcome to Our Platform!</h2>
        <p>Thank you for signing up. We’re thrilled to have you!</p>
        <p>Let us know if you have any questions or need help getting started.</p>
        <br>
        <p style="color: #7f8c8d;">Cheers,<br>The Team</p>
      </body>
    </html>
    """

    try:
        logger.info(f"Sending welcome email to {email}")
        send_mail(
        subject=subject,
        message=message,
        from_email=None,  # Uses DEFAULT_FROM_EMAIL from settings
        recipient_list=[email],
        fail_silently=False,
        html_message=html_message
      )
    except SMTPException as exc:
        # Retry after default_retry_delay (10 seconds)
        logger.warning(f"Retrying email to {email} due  to error: {exc}")
        raise self.retry(exc=exc)


@shared_task
def send_otp_email_task(self,email,username, otp_code):
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