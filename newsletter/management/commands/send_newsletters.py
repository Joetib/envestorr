from django.core.management.base import BaseCommand

from django.utils import timezone
from newsletter.utils import send_all_newsletters
class Command(BaseCommand):
    help = "Send Unsent newsletters to subscribers"

    def handle(self, *args, **kwargs):
        time = timezone.now()
        self.stdout.write(f"Running NewsLetter delivery background tasks: {time}")
        send_all_newsletters()
        end_time = timezone.now()
        self.stdout.write(f"Completed running NewsLetter delivery background tasks : {end_time}")