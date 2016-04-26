from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.TextField()

    def __str__(self):
        return "%s" % (self.name)


class Employee(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    position = models.ForeignKey(Position, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)