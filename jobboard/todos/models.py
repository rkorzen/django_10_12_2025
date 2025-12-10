from django.db import models
from dataclasses import dataclass
# Create your models here.

@dataclass
class Todo:
    id: int
    title: str
    description: str


baza = [Todo(1, "A", "ABC"), Todo(2, "B", "ABCD")]