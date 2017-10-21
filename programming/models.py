from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Programming(models.Model):
    nama = models.CharField(max_length=100)
    describ = models.CharField(max_length=100)
    

    def __unicode__(self):
        return self.nama