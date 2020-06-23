import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","vjproject.settings")
import django
django.setup()
from testapp.models import *
from faker import Faker

from random import *
f=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=f.date()
        fcompany=f.company()
        ftitle=f.random_element(elements=('Project Manger','Team Lead','Software Engg'))
        feligibility=f.random_element(elements=('Btech','Mtech','MCA','Phd'))
        faddress=f.address()
        femail=f.email()
        fphonenumber=phonenumbergen()
        chennaijobs_record=chennaijobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
populate(25)
