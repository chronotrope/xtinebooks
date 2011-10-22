from django.db import models

# Create your models here.
class BlogPost(models.Model):
    book_title = models.CharField(max_length=150)
    book_author = models.CharField(max_length=150)
    book_desc = models.TextField()
    isbn = models.CharField(max_length=150)
    rating = models.IntegerField()
    image_url = models.CharField(max_length=150)


