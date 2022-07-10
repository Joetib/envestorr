from django.core.management.base import BaseCommand

from django.utils import timezone
from financial_tools.utils import fetch_rates

class Command(BaseCommand):
    help = "Fetch currency updates in background tasks"

    def handle(self, *args, **kwargs):
        time = timezone.now()
        self.stdout.write(f"Running News background tasks: {time}")
        fetch_rates()
        end_time = timezone.now()
        self.stdout.write(f"Completed running News background tasks : {end_time}")