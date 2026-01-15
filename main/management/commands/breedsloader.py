from django.core.management import BaseCommand
import requests
from main.models import DogBreed


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--key', type=str, required=True)

    def handle(self, *args, **options):
        key = options['key']
        offset = 0
        while True:
            response = requests.get(
                'https://api.api-ninjas.com/v1/dogs',
                headers={'X-Api-Key': key},
                params={
                    'min_weight': 1,
                    'offset': offset
                },
                verify=False
            )
            if response.status_code != 200:
                break
            dogs = response.json()
            if not dogs:
                break
            for dog in dogs:
                DogBreed.objects.update_or_create(
                    name=dog['name'],
                    min_weight=dog['min_weight_male'],
                    max_weight=dog['max_weight_male'],
                    shedding=dog['shedding'],
                    grooming=dog['grooming'],
                    energy=dog['energy'],
                    trainability=dog['trainability'],
                    good_with_children=dog['good_with_children'],
                    good_with_other_dogs=dog['good_with_other_dogs'],
                    dog_photo=dog['image_link']
                )
            offset += 20
