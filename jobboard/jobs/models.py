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