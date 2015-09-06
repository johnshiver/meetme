from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings

from model_utils.models import TimeStampedModel


class UserProfile(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    # location information
    zipcode = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=128, blank=False)
    state = models.CharField(max_length=64, blank=False)




