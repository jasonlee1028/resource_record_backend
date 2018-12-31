from django.db import models

# Create your models here.


class VisitorRecord(models.Model):
    ip_address = models.CharField(max_length=64, default=None)
    access_index = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.access_index}:{self.ip_address}'
