from django.core.management.base import BaseCommand, CommandError
from filler.openfoodfacts.database import OFFDatabase

class Command(BaseCommand):

    help = 'Update the database.'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):

        # Init OFFDatabase
        database = OFFDatabase()

        # Test Connexion
        if database.get_connexion():

            print('Fetching OpenFoodFacts Database...')

            # Update Database
            database.update_database()

            # Test Database
            if len(database.searchs) > 0:
                try:
                    # Update Django
                    database.update_django()
                    self.stdout.write(self.style.SUCCESS('Django Updated'))
                except:
                    raise CommandError('Django not Updated')
            else:
                raise CommandError('Error while updating database')

        else:
            raise CommandError('OpenFoodFacts not reachable')
