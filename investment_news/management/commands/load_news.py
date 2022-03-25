from django.core.management.base import BaseCommand

from django.utils import timezone
from investment_news.utils import run

class Command(BaseCommand):
    help = "Run background tasks"

    def handle(self, *args, **kwargs):
        time = timezone.now()
        self.stdout.write(f"Running News background tasks: {time}")
        run()
        end_time = timezone.now()
        self.stdout.write(f"Completed running News background tasks : {end_time}")