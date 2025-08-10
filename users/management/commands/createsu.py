from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import os


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        try:
            if not User.objects.filter(username=os.environ.get("AD_USERNAME")).exists():
                user = User.objects.create_superuser(
                    username=os.environ.get("AD_USERNAME"),
                    email=os.environ.get("AD_EMAIL"),
                    password=os.environ.get("AD_PASSWORD"),
                )
                user.save()
                print(
                    "Superuser has been created!!",
                    user,
                    user.password,
                    os.environ.get("AD_USERNAME"),
                    os.environ.get("AD_PASSWORD"),
                )
            else:
                print("Couldn't create superuser")
        except Exception as e:
            print(e)
