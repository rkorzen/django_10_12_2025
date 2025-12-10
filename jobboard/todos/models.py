from django.db import models
from dataclasses import dataclass
# Create your models here.
#
# @dataclass
# class Todo:
#     id: int
#     title: str
#     description: str
#
#
# baza = [Todo(1, "A", "ABC"), Todo(2, "B", "ABCD")]
baza = []

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_done = models.BooleanField(default=False)