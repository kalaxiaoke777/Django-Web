from django.contrib.gis.db import models as PGmodels


class Fish(PGmodels.Model):
    class Meta:
        verbose_name_plural = "fishes"
