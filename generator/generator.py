from faker.contrib.pytest.plugin import faker
from faker.generator import random

from data.data import Person
from faker import Faker

faker_en = Faker('En')

def genetared_person():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject='English'
    )

def generate_file():
    path = rf'D:\PyCharm\project\test{random.randint(10, 100)}.txt'
    file = open(path, 'w')
    file.write(f'Dex{random.randint(1, 100)}')
    file.close()
    return path