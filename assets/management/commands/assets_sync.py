#

from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        print("sync assets with MSSQL")
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)