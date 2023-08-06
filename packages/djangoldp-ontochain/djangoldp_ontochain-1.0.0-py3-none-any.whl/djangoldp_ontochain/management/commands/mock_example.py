from django.core.management.base import BaseCommand, CommandError
from djangoldp_ontochain.factories import WalletFactory

class Command(BaseCommand):
    help = 'Mock data'

    def add_arguments(self, parser):
        parser.add_argument('--size', type=int, default=0, help='Number of ontochain to create')

    def handle(self, *args, **options):
        WalletFactory.create_batch(options['size'], thread=thread)
        self.stdout.write(self.style.SUCCESS('Successful data mock install'))
