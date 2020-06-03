from django.core.management.base import BaseCommand, CommandError
from .openfoodfacts.database import OFFDatabase

class Command(BaseCommand):

    help = 'Update the database.'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):

        database = OFFDatabase()

        if database.get_connexion():
            pass
        else
            raise CommandError('OpenFoodFacts not reachable')
