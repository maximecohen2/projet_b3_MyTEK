from django.db import models

from media.models.media import Media


class Episode(models.Model):
    media = models.OneToOneField(
        Media,
        verbose_name="Media",
        on_delete=models.CASCADE
    )

    number = models.IntegerField(
        verbose_name="Numéro de l'épisode"
    )

    season = models.IntegerField(
        verbose_name="Saison de l'épisode"
    )

    serie = models.ForeignKey(
        Media,
        verbose_name="Série",
        on_delete=models.CASCADE,
        related_name="+"
    )
