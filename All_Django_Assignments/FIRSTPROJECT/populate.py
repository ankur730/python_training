import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FIRSTPROJECT.settings')

import django
django.setup()

from FIRSTAPP.models import Detail
from faker import Faker
from random import *

fake = Faker()

def phone_number():
    num =''
    d1 = randint(6,9)
    num = num + str(d1)
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)


def populate(n):
    for i in range(n):
        fname = fake.name()
        fcontact = phone_number()
        faddress = fake.address()

        detail_record = Detail.objects.get_or_create(name=fname,contact=fcontact,address=faddress)

populate(30)


