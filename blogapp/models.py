from django.utils import timezone
from django.db import models
from django.conf import settings

class Post(models.Model):   # Capital P (best practice)

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=150, blank=True)
    publish = models.DateField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_post',
        null=True,
        blank=True
    )
    content = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
