from django.db import models

class WatchList(models.Model):
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.title