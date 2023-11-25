from django.core.management.base import BaseCommand
from myapp.models import State, LGA, Ward, PollingUnit, AnnouncedPuResult


class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        self.populate_states()

    def populate_states(self):
        delta_state = State.objects.create(name='Delta State')
        lga = LGA.objects.create(name='Sample LGA', state=delta_state)
        ward = Ward.objects.create(name='Sample Ward', lga=lga)
        polling_unit = PollingUnit.objects.create(
            name='Sample Polling Unit', ward=ward)

        self.create_announced_pu_results(polling_unit)

    def create_announced_pu_results(self, polling_unit):
        parties = ['PDP', 'DPP', 'ACN', 'PPA', 'CDC', 'JP']
        for party in parties:
            AnnouncedPuResult.objects.create(
                polling_unit=polling_unit, party=party, party_score=500)
