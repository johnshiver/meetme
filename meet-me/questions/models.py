from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings

from model_utils.models import TimeStampedModel


class Question(TimeStampedModel):

    answer_choices = (
        (0, "Yes"),
        (1, "No"),
    )

    answer_weights = (
        (1, "A little"),
        (2, "Somewhat"),
        (3, "Very")
    )

    question_types = (
        (0, "Personality"),
        (1, "Interest")
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.CharField(max_length=75)
    answer = models.IntegerField(choices=answer_choices)
    answer_weight = models.IntegerField(choices=answer_weights)
    question_type = models.IntegerField(choices=question_types)
