from django.db import models


class UserAgeData(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name
