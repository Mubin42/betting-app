from django.db import models

# Create your models here.
class Group(models.Model):
    name        = models.CharField(max_length=32, null=False, unique=False)
    location    = models.CharField(max_length=32, unique=False)
    description = models.CharField(max_length=255, null=False, unique=False)

    class Meta:
        unique_together = (('name', 'location'))
