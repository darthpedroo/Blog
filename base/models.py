from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=100)

class Paragraph(models.Model):
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    index_order = models.BigIntegerField()
    image_url = models.TextField(default=None)

class Image(models.Model):
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    




