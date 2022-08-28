"""Django command to wait until the database is available."""
from time import sleep

from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Entrypoint for the command"""
        db_up = False
        self.stdout.write("waiting for Database")
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database is unavailable sleep for 2s")
                sleep(2)
        self.stdout.write(self.style.SUCCESS("Database is available."))
