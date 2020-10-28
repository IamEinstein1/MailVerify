from datetime import datetime, timezone
from django.db import models

# Create your models here.


class Id(models.Model):
    unique_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(default=datetime.now(tz=timezone.utc))
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=30)
    mail = models.CharField(max_length=100)
    mail_is_real = models.BooleanField(default=False, blank=False)
    ip = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"ID - {self.unique_id}\n TIME - {self.time_created}"


class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=30)
    mail = models.CharField(max_length=100)
