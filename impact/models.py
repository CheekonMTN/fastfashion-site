from django.db import models

class HeadlineStat(models.Model):
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    source = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title
