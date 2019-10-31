import os
os.environ.setdefault('DJANGO_SETTINGS_MODULES','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, WebPage, Topic 
from faker import Faker 


fakegen = Faker()
topics = ['Search', 'Dating Apps', 'Games', 'News']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    return t.save()

def populate(N=5):

    for entry in range(N):
        # Get the topic for the entry
        top = add_topic()

        # Faker 
        faker_ulr = fakegen.url()
        fake_data = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry 
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)

if __name__ == '__main__':
    print("Faker script!")
    populate(20)
    print("Faker is done!")
