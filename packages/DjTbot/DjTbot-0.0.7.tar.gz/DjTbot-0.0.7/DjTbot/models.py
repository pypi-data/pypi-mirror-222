from django.db import models


class TBotUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    groups = models.ManyToManyField('TBotGroup', blank=True)

    def __str__(self):
        return f'{self.name}  ({self.id})'


class TBotGroup(models.Model):
    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return f'{self.name}'
