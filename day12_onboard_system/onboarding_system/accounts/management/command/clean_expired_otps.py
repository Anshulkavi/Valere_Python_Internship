from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from accounts.models import OTP

class Command(BaseCommand):
    help = 'Clean expired OTP codes'

    def handle(self, *args, **options):
        expired_time = timezone.now() - timedelta(minutes=5)
        expired_otps = OTP.objects.filter(created_at__lt=expired_time)
        count = expired_otps.count()
        expired_otps.delete()
        self.stdout.write(
            self.style.SUCCESS(f'Successfully deleted {count} expired OTP(s)')
        )