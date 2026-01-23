from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.conf import settings

class Post(models.Model):   # Capital P (best practice)

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status = 'published')
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    slug = models.SlugField(max_length=150, blank=True , unique=True)
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
    objects = models.Manager()
    newmanager = NewManager()
    
    def get_absolute_url(self):
        return reverse('blogapp:post_single' , args=[self.slug])
        
    
    class meta:
        ordering = ('publish')
        
        
    def __str__(self):
        return self.title
