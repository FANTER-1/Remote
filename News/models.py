from django.db import models

class News(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    text = models.TextField()

    def __str__(self):
        return self.title