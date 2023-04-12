from django.db import models


class MixList(models.Model):

    creator_id = models.ForeignKey(
        "creator", on_delete=models.CASCADE, related_name='creator_of_mix_list')
    name = models.CharField(max_length=200)
