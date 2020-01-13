from django.db import models


class Event(models.Model):
    name = models.TextField(max_length=30, blank=True)
    class_name = models.IntegerField()
    class_letter = models.TextField(max_length=2, blank=True)
    date = models.DateField()
