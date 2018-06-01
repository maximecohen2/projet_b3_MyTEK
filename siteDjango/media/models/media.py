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

    type = models.IntegerField(choices=MEDIA_TYPE)
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    image = models.ImageField(upload_to='/media')
    nationality = models.IntegerField(choices=NATIONALITY)
    originale_title = models.CharField(max_length=100)
    release_date = models.DateField()
    pegi_certification = models.IntegerField()
