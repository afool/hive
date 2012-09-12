from django.core.management.base import BaseCommand
from admins.tasks import excute_post_humorbot

class Command(BaseCommand):
    def handle(self, *args, **options):
        excute_post_humorbot()
        print "command is excuted"
     
