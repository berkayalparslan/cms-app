from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    publish_date = models.DateTimeField("publish date")
    slug = models.SlugField(null=True, unique=True)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='posts')

    def save(self, *args, **kwargs):
        self.publish_date = datetime.now()
        if not self.slug:
            timestamp = int(datetime.timestamp(self.publish_date))
            self.slug = slugify(self.title + '-'+ str(timestamp))
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'Comment by {self.user.username} on {self.post}'

