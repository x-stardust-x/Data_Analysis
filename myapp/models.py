from django.db import models

# Create your models here.


class task(models.Model):
    uuid = models.CharField(max_length=10, null=False)
    email = models.EmailField(max_length=20, null=False)
    type = models.CharField(max_length=10, null=False)
    name = models.CharField(max_length=10, blank=True, default='')
    token = models.CharField(max_length=20, blank=True, default='')
    overview = models.CharField(max_length=255, blank=True, default='')
    cover = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name
