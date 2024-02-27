from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)

class Paragraph(models.Model):
    articleId = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    index_order = models.BigIntegerField()


    

