from questions.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('email', type=str)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = options['email']
        try:
            user = User.objects.create_user(username,email,password)
            user.save()
        except:
            print("can't create user")
