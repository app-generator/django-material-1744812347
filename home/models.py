# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    unit_number = models.IntegerField(null=True, blank=True)
    driver = models.TextField(max_length=255, null=True, blank=True)
    division = models.TextField(max_length=255, null=True, blank=True)
    year = models.TextField(max_length=255, null=True, blank=True)
    mileage = models.IntegerField(null=True, blank=True)
    make = models.TextField(max_length=255, null=True, blank=True)
    model = models.TextField(max_length=255, null=True, blank=True)
    license = models.TextField(max_length=255, null=True, blank=True)
    vin = models.TextField(max_length=255, null=True, blank=True)
    inspection = models.DateTimeField(blank=True, null=True, default=timezone.now)
    color = models.TextField(max_length=255, null=True, blank=True)
    gate_tag = models.TextField(max_length=255, null=True, blank=True)
    radio_serial = models.TextField(max_length=255, null=True, blank=True)
    radio_id = models.TextField(max_length=255, null=True, blank=True)
    replacement = models.TextField(max_length=255, null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__

#__MODELS__END
