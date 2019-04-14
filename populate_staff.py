import os, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'abz_test.settings')

import django
django.setup()

from django_seed import Seed
from staff.models import Boss, Employee

def populate():
    seeder = Seed.seeder()
    seeder.add_entity(Boss, 5000, {
        'full_name': lambda x: seeder.faker.first_name() + ' ' + seeder.faker.last_name(),
    })
    seeder.add_entity(Employee, 50000, {
        'boss': lambda x: Boss.objects.get(id=random.randint(1, 5000)),
        'full_name': lambda x: seeder.faker.first_name() + ' ' + seeder.faker.last_name(),
        'job': lambda x: seeder.faker.sentence(),
        'salary': lambda x: random.randrange(1, 10000),
    })

    inserted_pks = seeder.execute()

if __name__ == '__main__':
    populate()