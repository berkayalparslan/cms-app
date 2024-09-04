from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    publish_date = models.DateTimeField("publish date")
    slug = models.SlugField(null=True, unique=True)

    def save(self, *args, **kwargs):
        self.publish_date = datetime.now()
        if not self.slug:
            timestamp = datetime.timestamp(self.publish_date)
            self.slug = slugify(self.title + '-'+ str(timestamp))
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})
    
