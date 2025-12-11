from django.db import models

class RecruiterProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=140, blank=True )
    email = models.EmailField(blank=True)


class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    size = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("tags.Tag", blank=True)
    recruiter = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="offers")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def info(self):
        return f"{self.title} {self.description}"

    def __str__(self):
        return self.title