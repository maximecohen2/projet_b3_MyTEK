from django.db import models

# Create your models here.


class Group(models.Model):
    label = models.CharField(
        verbose_name="Nom du groupe",
        max_length=100
    )