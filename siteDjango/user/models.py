from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="Utilisateur",
        on_delete=models.CASCADE
    )

    firstname = models.CharField(
        verbose_name="Prénom",
        max_length=50
    )

    lastname = models.CharField(
        verbose_name="Nom",
        max_length=50
    )

    image = models.ImageField(
        verbose_name="Image de profil",
        upload_to="person",
        null=True
    )

    birthday = models.DateField(
        verbose_name="Date de naissance",
        null=True
    )

    # mediatek = models.OneToOneField(
    #     verbose_name="Médiatek"
    # )