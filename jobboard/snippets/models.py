from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

LEXER = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = [(item[1][0], item[0]) for item in LEXER]
STYLE_CHOICES = [(item, item) for item in get_all_styles()]

class TimestampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Snippet(TimestampedMixin):
    title = models.CharField(max_length=255)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100, default="python", choices=LANGUAGE_CHOICES)
    style = models.CharField(max_length=100, default="friendly", choices=STYLE_CHOICES)

    class Meta:
        ordering = ["created_at"]