from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic_name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.PROTECT)
    date = models.DateField((""), auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.date)
    
