from django.db import models
from dataclasses import dataclass
# Create your models here.

@dataclass
class Job:
    id: int
    title: str
    description: str


    def info(self):
        return f"{self.title} {self.description}"

baza = [Job(1, "A", "ABC"), Job(2, "B", "ABCD")]


class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def info(self):
        return f"{self.title} {self.description}"