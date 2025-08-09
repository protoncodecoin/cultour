from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import os


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username=os.environ.get("AD_USERNAME"),
                email=os.environ.get("AD_EMAIL"),
                password=os.environ.get("AD_PASSWORD"),
            )
        print("Superuser has been created.")
