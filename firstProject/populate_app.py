import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'firstProject.settings')
django.setup()

import random
from firstApp.models import WebPage, AccessRecord, Topic, User
from faker import Faker

fake = Faker()
topics = ['Serach', 'Social', 'Market', 'News', 'Games']


def add_topics():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for i in range(N):
        top = add_topics()
        url = fake.url()
        date = fake.date()
        company = fake.company()
        page = WebPage.objects.get_or_create(top=top, url=url, name=company)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=page, date=date)[0]


def populate_users(N=10):
    for i in range(N):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]


if __name__ == '__main__':
    print("populating model")
    populate_users(20)
    print("Completed")
