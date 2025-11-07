from django.db import models
from django.utils.translation import gettext_lazy as _


class Produce(models.Model):
    name = models.CharField(_('name'), max_length=200)
    origin_village = models.CharField(_('origin_village'), max_length=200)

    def __str__(self):
        return self.name
