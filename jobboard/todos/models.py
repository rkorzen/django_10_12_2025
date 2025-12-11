from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("tags.Tag", blank=True)