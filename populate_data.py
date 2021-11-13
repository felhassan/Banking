import django

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import CustomUser
from faker import Faker
fake= Faker()
def populateCustomUser(number_of_user=100):
    for cust in range(number_of_user):
        fake_name=fake.name()
        fake_lastname=fake.name()
        fake_email=fake.email()
        custom_user=CustomUser.objects.get_or_create(first_name=fake_name,last_name=fake_lastname,email=fake_email)[0]
        custom_user.save()

if __name__== "__main__":
    populateCustomUser(100)