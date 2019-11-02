import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")
django.setup()

from first_app.models import AccessRecord, WebPage, Topic 
from faker import Faker 

fakegen = Faker()
topics = ['Search', 'Dating Apps', 'Games', 'News']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t 

def populate(N=5):

    for entry in range(N):
        # Get the topic for the entry
        top = add_topic()

        # Faker 
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry 
        webpg = WebPage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        
        # Create a fake access record for that webage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)

if __name__ == '__main__':
    print("Faker script!")
    populate(20)
    print("Faker is done!")
