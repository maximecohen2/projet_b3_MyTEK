from django.db import models

from siteDjango.media.models.media import Media
from siteDjango.media.models.serie import Serie


class Episode(models.Model):
    media = models.OneToOneField(Media)
    number = models.IntegerField()
    season = models.IntegerField()
    series = models.OneToOneField(Serie)
