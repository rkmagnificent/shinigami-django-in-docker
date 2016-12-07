from django.db import models


class DeathNote(models.Model):
    person_name = models.TextField()
    cause_of_death = models.TextField(null=True)
    datetime_of_death = models.DateTimeField(null=True)
    entry_datetime = models.DateTimeField(auto_now_add=True)


class AddedLifeSpan(models.Model):
    deathnote_entry = models.ForeignKey(DeathNote, on_delete=models.CASCADE)
    life_added = models.IntegerField(default=0)
    life_added_datetime = models.DateTimeField(auto_now_add=True)
