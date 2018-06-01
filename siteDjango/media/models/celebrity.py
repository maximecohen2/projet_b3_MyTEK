from django.db import models

from siteDjango.user.models import Person


class Celebrity(models.Model):
    bio = models.TextField()
    person = models.OneToOneField(Person)
