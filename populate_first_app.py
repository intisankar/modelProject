import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelProject.settings')

import django
django.setup()

# FAKE POP Script
import random
from testApp.models import Employee

from faker import Faker

fakegen = Faker()
ename = ['sankar','sai','shahid','raj']


def add_employee():
    fake_eaddr = fakegen.address()
    fake_eno = fakegen.msisdn()
    fake_ename = fakegen.first_name()
    fake_esal = fakegen.msisdn()

    t = Employee.objects.get_or_create(ename=random.choice(ename),eno=fake_eno,esal=fake_esal,eaddr=fake_eaddr)[0] #return the tupple and grab the second element
    t.save()
    return t
    
# how many times inwich it is to be run
def populate(N=5):
    for entry in range(N):
        add_employee()


if __name__ == '__main__':
    print ("populating Data!..")
    populate(20)
    print("populate completed!.")
