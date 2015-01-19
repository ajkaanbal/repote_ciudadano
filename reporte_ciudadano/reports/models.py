from django.db import models

# Create your models here.


class Report(models.Model):
    TYPES = (
        (0, 'proposal'),
        (1, 'wish'),
        (2, 'participate'),
    )

    kind = models.PositiveSmallIntegerField(choices=TYPES)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    address = models.CharField(max_length=128)
    # location
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

