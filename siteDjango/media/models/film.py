from django.db import models

class film(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)