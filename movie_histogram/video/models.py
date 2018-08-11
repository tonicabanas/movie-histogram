from model_utils.models import TimeStampedModel
from django.db import models


class Video(TimeStampedModel):
    file = models.CharField(max_length=30)


class Histogram(TimeStampedModel):
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'
    GREYSCALE = 'GS'
    COLOR = (
        (RED, 'Red'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (GREYSCALE, 'Greyscale'),
    )
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    t = models.IntegerField()
    num_bin = models.IntegerField()
    bin_value = models.FloatField()
    color = models.CharField(max_length=10, choices=COLOR)
