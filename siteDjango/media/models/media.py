from django.db import models


class Media(models.Model):
    MEDIA_TYPE = (
        ('M', 'Film'),
        ('S', 'Serie'),
        ('E', 'Episode'),
    )

    NATIONALITY = (
        ('FR', 'France'),
        ('US', 'Etats-Unies'),
    )

    type = models.IntegerField(
        verbose_name="Type de Media",
        choices=MEDIA_TYPE
    )

    title = models.CharField(
        verbose_name="Titre du Media",
        max_length=100
    )

    synopsis = models.TextField(
        verbose_name="Synopsis",
        null=True,
        blank=True
    )

    image = models.ImageField(
        verbose_name="Image",
        null=True,
        blank=True
    )

    nationality = models.IntegerField(
        verbose_name="Nationalité",
        choices=NATIONALITY,
        null=True,
        blank=True
    )

    originale_title = models.CharField(
        verbose_name="Titre original",
        max_length=100,
        null=True,
        blank=True
    )

    release_date = models.DateField(
        verbose_name="Date de sortie",
        null=True,
        blank=True
    )

    pegi_certification = models.IntegerField(
        verbose_name="Certification",
        null=True,
        blank=True
    )

