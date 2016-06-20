from __future__ import unicode_literals

from django.db import models


class TestModel(models.Model):
    id = models.IntegerField(primary_key=True)
    f1 = models.CharField(max_length=255)
    f2 = models.IntegerField()
    f3 = models.TextField()
    f4 = models.IntegerField()

    class Meta:
        db_table = 'test_table'
