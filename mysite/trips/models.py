from django.utils import timezone
from django.db import models
#放進圖片
# Create your models here.

class Photo(models.Model):
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)
# 放進圖片

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title