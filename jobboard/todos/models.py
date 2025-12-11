from django.db import models



class Todo(models.Model):

    STATUS_CHOICES = (
        ("planned", "Planned"),
        ("during", "During"),
        ("done", "Done"),
        ("canceled", "Canceled"),
        ("blocked", "Blocked")
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("tags.Tag", blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="planned")

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"