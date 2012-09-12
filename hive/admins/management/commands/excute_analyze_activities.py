from django.core.management.base import BaseCommand
from admins.tasks import execute_analyze_activities

class Command(BaseCommand):
    def handle(self, *args, **options):
        execute_analyze_activities()
        print "command is excuted"
    