from django.db import models


class Mood(models.Model):

    name = models.CharField(max_length=500)
