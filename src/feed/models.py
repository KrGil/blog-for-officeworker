from django.db import models

# Create your models here.
class Article(models.Model):
    DEVELOPMET = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMET, "dvelopment"),
        (PERSONAL, "personal"),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMET,
    )

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

class HashTag(models.Model):
    name = models.CharField(max_length=50)
